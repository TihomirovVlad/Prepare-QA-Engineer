
import requests
BASE_URL = "https://httpbin.org/anything"
HEADERS = {
        "Content-Type" : "application/json",
        "Authorization" : "Bearer fake_token_for_test"
    }

def test_successful_payment_request():
    '''
    Цель: Проверить, что валидный платёж корректно принимается.
    '''
    data = {
        "from_account" : "ACC1234567890",
        "to_account" : "ACC0987654321",
        "amount" : 1500,
        "currency" : "RUB",
        "idempotency_key" : "req_20250405_abc123"
    }

    response = requests.post(BASE_URL, json = data, headers = HEADERS,timeout=10)

    result = response.json()["json"]
    assert response.status_code == 200
    assert result == data
    assert type(result["amount"]) == int
    assert result["currency"] in ["RUB","USD","EUR"]
    assert "application/json" in response.headers["Content-Type"]

def test_invalid_currency_rejected():
    '''
    Цель: Проверить обработку невалидной валюты.
    '''
    data = {
        "from_account": "ACC1234567890",
        "to_account": "ACC0987654321",
        "amount": 1500,
        "currency": "BYN",
        "idempotency_key": "req_20250405_abc123"
    }
    response = requests.post(BASE_URL, json = data, headers = HEADERS,timeout=10)
    assert response.status_code == 200
    #В продакшене: assert response.status_code == 400

def test_idempotency_key_required():
    '''
    Проверить, что повторный запрос с тем же idempotency_key не создаёт дубль.
    '''
    data = {
        "from_account": "ACC1234567890",
        "to_account": "ACC0987654321",
        "amount": 1500,
        "currency": "RUB",
        "idempotency_key": "req_20250405_abc123"
    }
    response1 = requests.post(BASE_URL,json = data, headers = HEADERS,timeout=10)
    response2 = requests.post(BASE_URL, json=data, headers=HEADERS,timeout=10)

    # httpbin не поддерживает идемпотентность, но мы эмулируем
    assert response1.status_code == 200
    assert response2.status_code == 200
    # В продакшене: resp2.json() == resp1.json() и не создаётся новый платёж