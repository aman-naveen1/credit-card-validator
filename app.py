"""Streamlit interface for the credit-card validator."""

import streamlit as st

from validator import validate_card

st.set_page_config(page_title="Credit Card Validator", page_icon="💳", layout="centered")

st.title("💳 Credit Card Validator")
st.caption("Validate a card-number format and Luhn checksum locally.")

st.info(
    "Use only public test numbers in this demo. Never enter a real payment-card number. "
    "A successful Luhn check does not mean a card exists, is active, funded, or authorized."
)

card_number = st.text_input(
    "Card number",
    placeholder="e.g. 4242 4242 4242 4242",
    type="password",
)

if st.button("Validate", type="primary", use_container_width=True):
    if not card_number.strip():
        st.warning("Please enter a card number.")
    else:
        result = validate_card(card_number)

        if result["valid"]:
            st.success("✓ Card number passes the Luhn check")
        else:
            st.error("✗ Card number failed validation")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Network", result["network"])
        with col2:
            st.metric("Length", result["length"])

        st.write(f"**Luhn check:** {'Passed' if result['luhn_passed'] else 'Failed'}")
        st.write(f"**Masked value:** `{result['masked']}`")

st.divider()
st.subheader("How it works")
st.markdown(
    """
1. Spaces and hyphens are removed.
2. The number is checked for a 12–19 digit format.
3. Every second digit from the right is doubled.
4. Values above 9 are reduced by 9.
5. All resulting digits are summed.
6. A total divisible by 10 passes the Luhn checksum.

The Luhn algorithm is a checksum, not a payment authorization mechanism.
"""
)
