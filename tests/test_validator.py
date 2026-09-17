import pytest

from validator import detect_card_network, luhn_check, mask_card_number, normalize_card_number, validate_card


@pytest.mark.parametrize(
    "number",
    [
        "4242424242424242",
        "4242 4242 4242 4242",
        "5555555555554444",
        "378282246310005",
        "6011111111111117",
    ],
)
def test_valid_luhn_numbers(number):
    assert luhn_check(number) is True


def test_invalid_checksum():
    assert luhn_check("4242424242424243") is False


def test_normalization():
    assert normalize_card_number(" 4242-4242 4242-4242 ") == "4242424242424242"


def test_invalid_characters_and_length():
    assert luhn_check("abcd424242424242") is False
    assert luhn_check("12345678901") is False


def test_network_detection():
    assert detect_card_network("4242424242424242") == "Visa"
    assert detect_card_network("5555555555554444") == "Mastercard"
    assert detect_card_network("378282246310005") == "American Express"
    assert detect_card_network("6011111111111117") == "Discover"


def test_masking():
    assert mask_card_number("4242424242424242") == "************4242"


def test_structured_validation():
    result = validate_card("4242 4242 4242 4242")
    assert result["valid"] is True
    assert result["network"] == "Visa"
    assert result["length"] == 16
    assert result["luhn_passed"] is True
