import requests

def test_payment_payload_is_echoed():
    url = "https://httpbin.org/anything"
    payload = {
        "from" : "ACC1",
        "to" : "ACC2",
        "amount" : 100,
        "currency" : "RUB"
    }

    response = requests.post(url, json = payload , timeout = 10)
    assert response.status_code == 200

    echoed = response.json()["json"]
    assert echoed == payload