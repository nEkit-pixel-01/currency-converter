from converter import convert

def test_convert_positive_amount():
    result = convert(100, "USD", "USD")
    assert result == 100.0

def test_convert_negative_amount_return_none():
    result = convert(-50, "USD", "RUB")
    assert result is None

def test_convert_non_number_return_none():
    result = convert("сто", "USD", "KZT")
    assert result is None