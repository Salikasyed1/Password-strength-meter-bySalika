import streamlit as st

def check_passwod(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔴Use at least 8 characters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("🟠Include upper letter.")
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("🟡Include lower letter.")
    if any (c.isdigit() for c in password):
        score += 1
    else:
        tips.append("🔵Add a number (0-9).")
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append("🟣Use a special character (!@#$%^&*).")
    return score, tips

def main():
    st.title("🔐Password Strength Meter")
    password = st.text_input("Enter Password 🔑", type="password")

    if password:
        score, tips = check_passwod(password)

        if score == 5:
            st.success("✅Strong Password! Secure & Safe.")
        elif score == 3 or score == 4:
            st.warning("⚠️Moderate Password! Improve it.")
        else:
            st.error("❌Weak Pasword! Follow these steps:")
        for tip in tips:
            st.write(tip)

main()