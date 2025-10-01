def validate_transfer(amount, currency):
    return amount>0 and currency in ["RUB", "USD", "EUR"]

def test_validate_transfer_positive_rub():
    assert validate_transfer(1, "RUB") is True

def test_validate_transfer_negative_byn():
    assert validate_transfer(1,"BYN") is False

def test_validate_transfer_zero_amount():
    assert validate_transfer(0, "USD") is False

def test_validate_transfer_negative_amount():
    assert validate_transfer(-50, "EUR") is False

def test_validate_transfer_invalid_currency_string():
    assert validate_transfer(100, "RUB,BYN") is False