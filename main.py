import requests

def send_payment(data):
    return requests.post(url, json=data)

url = "https://httpbin.org/anything"  # ← убраны пробелы!
payload = {
    "from": "ACC1",
    "to": "ACC2",
    "amount": 100,  # ← лучше int или строка в реальных платежах
    "currency": "RUB"
}

response = send_payment(payload)
assert response.status_code == 200, f"Expected 200, got {response.status_code}"

returned_data = response.json()["json"]
assert returned_data == payload, f"Payload mismatch: {returned_data} != {payload}"

print("✅ Тест пройден: платёж отправлен и корректно принят")
