import requests
import pytest
import json

# Базовый URL API
BASE_URL = "https://api.bank.example.com"


class BankAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {"Content-Type": "application/json"}

    def create_user(self, name: str, email: str) -> dict:
        """Создание пользователя"""
        payload = {"name": name, "email": email}
        response = requests.post(f"{self.base_url}/users", json=payload, headers=self.headers)
        return response

    def get_user_balance(self, user_id: str) -> dict:
        """Получение баланса пользователя"""
        response = requests.get(f"{self.base_url}/users/{user_id}/balance")
        return response

    def deposit_money(self, user_id: str, amount: float, currency: str = "RUB") -> dict:
        """Пополнение счета"""
        payload = {"amount": amount, "currency": currency}
        response = requests.post(
            f"{self.base_url}/users/{user_id}/deposit",
            json=payload,
            headers=self.headers
        )
        return response

    def transfer_money(self, from_user: str, to_user: str, amount: float) -> dict:
        """Перевод денег между пользователями"""
        payload = {
            "from_user_id": from_user,
            "to_user_id": to_user,
            "amount": amount,
            "currency": "RUB"
        }
        response = requests.post(
            f"{self.base_url}/transfers",
            json=payload,
            headers=self.headers
        )
        return response
