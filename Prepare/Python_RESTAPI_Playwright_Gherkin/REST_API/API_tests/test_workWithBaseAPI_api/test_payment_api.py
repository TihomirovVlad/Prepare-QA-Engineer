def test_payment_post_echoes_payload():
    import requests
    url = "https://httpbin.org/anything"

    transfer = {
        "from_account": "ACC123",
        "to_account": "ACC456",
        "amount": 1000,
        "currency": "RUB"
    }

    response = requests.post(url, json=transfer, timeout=10)

    assert response.status_code == 200
    assert response.json()["json"] == transfer
    assert response.headers["Content-Type"] == "application/json"

