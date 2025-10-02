import pytest
import requests

from BankApiClient import BankAPIClient
from BankApiClient import BASE_URL

@pytest.fixture
def api_client():
    return BankAPIClient(BASE_URL)


class TestBankingAPI:
    def test_complete_money_transfer_flow(self, api_client):
        """
        Полный тест перевода денег:
        1. Создать двух пользователей
        2. Пополнить счет первому пользователю
        3. Выполнить перевод
        4. Проверить балансы обоих пользователей
        """

        user1 = api_client.create_user("Vasya","testEmail123@mail.ru")
        user2 = api_client.create_user("Vova","test@inbox.ru")

        assert user1.status_code ==201
        assert user2.status_code ==201

        user1_id = user1.json()["id"]
        user2_id = user2.json()["id"]

        depositForUser1 = api_client.deposit_money(user1_id,1500.0)
        assert depositForUser1.status_code ==200

        transfer = api_client.transfer_money(user1_id,user2_id,800.0)

        assert transfer.status_code ==201

        balance1 = api_client.get_user_balance(user1_id)
        balance2 = api_client.get_user_balance(user2_id)

        assert balance1.json()["balance"] == 700
        assert balance2.json()["balance"] == 800



    def test_transfer_insufficient_funds(self, api_client):
        """
        Тест ошибки "недостаточно средств":
        1. Создать пользователя с нулевым балансом
        2. Попытаться выполнить перевод
        3. Проверить ошибку 402
        """

        user1 = api_client.create_user("Бедный чувак","poor@test.com")
        user2 = api_client.create_user("Богатый чувак", "rich@test.com")

        assert user1.status_code ==201
        assert user2.status_code ==201

        user1_id = user1.json()["id"]
        user2_id = user2.json()["id"]

        transfer = api_client.transfer_money(user1_id,user2_id,"400.0")
        assert transfer.status_code ==402

        assert "insufficient_funds" in transfer.json()["error_code"]
        pass

    def test_invalid_user_transfer(self, api_client):
        """
        Тест перевода несуществующему пользователю:
        1. Создать отправителя
        2. Попытаться перевести несуществующему получателю
        3. Проверить ошибку 404
        """

        user1 = api_client.create_user("Отправитель","dasdasd@mail.ru")
        assert user1.status_code ==201

        transfer = api_client.transfer_money(user1,"non_existent_user_id",1500.0)

        assert transfer.status_code == 404

        assert "user_not_found" in transfer.json()["error_code"]

    def test_transfer_validation_errors(self, api_client):
        """
        Тест валидации данных:
        1. Перевод отрицательной суммы
        2. Перевод нулевой суммы
        3. Невалидный JSON в запросе
        """

        user1 = api_client.create_user("Тестовый1", "test1@mail.ru")
        user2 = api_client.create_user("Тестовый2", "test2@mail.ru")
        user1_id = user1.json()["id"]
        user2_id = user2.json()["id"]

        transfer_negative = api_client.transfer_money(user1_id, user2_id, -100.0)
        assert transfer_negative.status_code == 400
        assert "invalid_amount" in transfer_negative.json()["error_code"]

        transfer_zero = api_client.transfer_money(user1_id, user2_id, 0.0)
        assert transfer_zero.status_code == 400
        assert "invalid_amount" in transfer_zero.json()["error_code"]


        invalid_payload = "{invalid json}"
        response = requests.post(
            f"{BASE_URL}/transfers",
            data=invalid_payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 400


    def test_response_structure_validation(self, api_client):
        """
        Тест структуры JSON ответов:
        1. Проверить что все успешные ответы имеют ожидаемую структуру
        2. Проверить что ошибки имеют поле 'error'
        3. Проверить типы данных в ответах
        """
        # ТВОЙ КОД ЗДЕСЬ
        pass