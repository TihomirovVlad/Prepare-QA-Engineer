from transfer_validation import find_first_rub_transfer

def test_finds_first_rub_transfer():
    api_response = {
        "user_id": "usr_789",
        "transfers": [
            {"id": "tr_001", "amount": 1500.0, "currency": "RUB", "status": "completed"},
            {"id": "tr_002", "amount": 200.0, "currency": "USD", "status": "pending"},
            {"id": "tr_003", "amount": 5000.0, "currency": "RUB", "status": "failed"}
        ],
        "total_count": 3
    }
    result = find_first_rub_transfer(api_response["transfers"])
    assert result is not None
    assert result["id"] == "tr_001"
    assert result["amount"] == 1500.0
    assert result["currency"] == "RUB"

def test_returns_none_when_no_rub():
    api_response = {
        "user_id": "usr_789",
        "transfers": [
            {"id": "tr_001", "amount": 1500.0, "currency": "BYN", "status": "completed"},
            {"id": "tr_002", "amount": 200.0, "currency": "USD", "status": "pending"},
            {"id": "tr_003", "amount": 5000.0, "currency": "BLG", "status": "failed"}
        ],
        "total_count": 3
    }
    result = find_first_rub_transfer(api_response["transfers"])
    assert result is None