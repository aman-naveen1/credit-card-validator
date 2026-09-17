"""Credit card number validation using the Luhn (Mod-10) algorithm."""

import re
from typing import Optional


def normalize_card_number(card_number: str) -> str:
    """Remove spaces and hyphens from a card number."""
    return re.sub(r"[ -]", "", card_number.strip())


def detect_card_network(card_number: str) -> str:
    """Return a best-effort card network based on common IIN prefixes."""
    number = normalize_card_number(card_number)

    if re.match(r"^4", number):
        return "Visa"
    if re.match(r"^(5[1-5]|2(2[2-9]|[3-6][0-9]))", number):
        return "Mastercard"
    if re.match(r"^3[47]", number):
        return "American Express"
    if re.match(r"^(6011|65|64[4-9])", number):
        return "Discover"
    if re.match(r"^35", number):
        return "JCB"
    if re.match(r"^(30[0-5]|36|38)", number):
        return "Diners Club"
    return "Unknown"


def luhn_check(card_number: str) -> bool:
    """Validate a digit string with the Luhn checksum."""
    number = normalize_card_number(card_number)

    if not number.isdigit() or len(number) < 12 or len(number) > 19:
        return False

    total = 0
    parity = len(number) % 2

    for index, digit in enumerate(number):
        value = int(digit)
        if index % 2 == parity:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0


def validate_card(card_number: str) -> dict:
    """Return structured validation information without exposing the full number."""
    normalized = normalize_card_number(card_number)
    valid_format = normalized.isdigit() and 12 <= len(normalized) <= 19
    valid_luhn = valid_format and luhn_check(normalized)

    return {
        "valid": valid_luhn,
        "network": detect_card_network(normalized) if valid_format else "Unknown",
        "length": len(normalized),
        "luhn_passed": valid_luhn,
        "masked": mask_card_number(normalized) if valid_format else "Invalid input",
    }


def mask_card_number(card_number: str) -> str:
    """Mask a card number, retaining only its last four digits."""
    number = normalize_card_number(card_number)
    if not number.isdigit():
        return "Invalid input"
    if len(number) <= 4:
        return "*" * len(number)
    return "*" * (len(number) - 4) + number[-4:]


if __name__ == "__main__":
    card = input("Enter a card number: ")
    result = validate_card(card)
    print(f"Status: {'Valid' if result['valid'] else 'Invalid'}")
    print(f"Network: {result['network']}")
    print(f"Length: {result['length']}")
    print(f"Luhn check: {'Passed' if result['luhn_passed'] else 'Failed'}")
    print(f"Card: {result['masked']}")
