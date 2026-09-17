# 💳 Credit Card Validator

A beginner-friendly Python project that validates payment-card number formatting and the **Luhn (Mod-10) checksum**, with card-network detection, unit tests, and a Streamlit interface.

> **Security note:** This project is for learning and testing only. Use public test numbers. Never enter real payment-card details into this application or commit them to GitHub.

## ✨ Features

- Luhn / Mod-10 checksum validation
- Accepts spaces and hyphens in input
- Basic 12–19 digit format validation
- Best-effort network detection for Visa, Mastercard, American Express, Discover, JCB, and Diners Club
- Masks the displayed card number to the final four digits
- Clean command-line interface
- Streamlit web interface
- Automated pytest test suite
- GitHub Actions CI

## 🧠 How the Luhn Algorithm Works

The Luhn algorithm is a checksum commonly used for payment-card numbers. The PCI Security Standards Council describes it as a way to determine whether a card number is mathematically possible; it does **not** establish that the card was actually issued or is active. [PCI Security Standards Council](https://www.pcisecuritystandards.org/faqs/1137/)

The implementation:

1. Removes spaces and hyphens.
2. Verifies that the input contains digits and is 12–19 digits long.
3. Starting from the right, doubles every second digit.
4. Subtracts 9 when a doubled value is greater than 9.
5. Adds all resulting values.
6. Checks whether the total is divisible by 10.

## 📁 Project Structure

```text
credit-card-validator/
├── validator.py                 # Luhn logic and network detection
├── app.py                       # Streamlit interface
├── requirements.txt
├── tests/
│   └── test_validator.py        # Automated tests
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions CI
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/aman-naveen1/credit-card-validator.git
cd credit-card-validator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the command-line validator

```bash
python validator.py
```

### 5. Run the web application

```bash
streamlit run app.py
```

### 6. Run tests

```bash
pytest -q
```

## 🧪 Test Numbers

Use only publicly documented test numbers for demonstrations. For example, payment processors such as Stripe publish test-card numbers for development. Do not substitute real personal card information.

## ⚠️ What This Project Does NOT Check

Passing the Luhn algorithm does **not** mean that:

- the card has actually been issued;
- the account is active;
- the card has available funds;
- a transaction will be authorized; or
- the number belongs to a particular person.

It is a mathematical checksum, not a payment authorization service.

## 🛠️ Technologies

- Python
- Regular expressions
- Luhn / Mod-10 checksum
- Streamlit
- pytest
- GitHub Actions

## 📌 Resume Bullet

**Credit Card Validator — Python**  
Built a credit-card validation utility implementing the Luhn (Mod-10) checksum, input normalization, card-network detection, masking, automated unit tests, and a Streamlit web interface with CI through GitHub Actions.

## 📚 References

- [PCI Security Standards Council — Luhn validation FAQ](https://www.pcisecuritystandards.org/faqs/1137/)
- [CyberSource — Luhn Mod-10 check digit scheme](https://developer.cybersource.com/docs/nab/en-us/test-data/developer/all/so/test-data/best_practices_intro/checking_digit_scheme.html)
