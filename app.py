import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SecurePass",
    page_icon="🔐",
    layout="centered",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
        body { background-color: #0d1117; }
        .main { background-color: #0d1117; }
        h1 { color: #58a6ff; text-align: center; }
        .subtitle { color: #8b949e; text-align: center; font-size: 0.95rem; margin-top: -10px; margin-bottom: 24px; }
        .strength-bar-container { background: #21262d; border-radius: 6px; height: 10px; margin: 8px 0 16px; }
        .strength-bar { height: 10px; border-radius: 6px; transition: width 0.4s ease; }
        .criteria-item { font-size: 0.88rem; padding: 2px 0; }
        .pass  { color: #3fb950; }
        .fail  { color: #f85149; }
        .tip-box { background: #161b22; border: 1px solid #30363d; border-radius: 8px;
                   padding: 14px 18px; margin-top: 16px; font-size: 0.88rem; color: #c9d1d9; }
        .tip-box b { color: #58a6ff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("# 🔐 SecurePass")
st.markdown(
    '<p class="subtitle">Real-time password strength analyser — cybersecurity project</p>',
    unsafe_allow_html=True,
)
st.divider()


# ── Strength analyser ──────────────────────────────────────────────────────────
def analyse(password):
    score = 0

    has_upper   = any(c.isupper() for c in password)
    has_lower   = any(c.islower() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?`~" for c in password)
    long_enough = len(password) >= 8
    very_long   = len(password) >= 12
    no_common   = password.lower() not in ["password", "123456", "qwerty", "admin", "letmein", "welcome"]

    if long_enough:   score += 1
    if very_long:     score += 1
    if has_upper:     score += 1
    if has_lower:     score += 1
    if has_digit:     score += 1
    if has_special:   score += 1
    if no_common:     score += 1

    checks = {
        "At least 8 characters":              long_enough,
        "At least 12 characters (recommended)": very_long,
        "Contains uppercase letter (A-Z)":    has_upper,
        "Contains lowercase letter (a-z)":    has_lower,
        "Contains digit (0-9)":               has_digit,
        "Contains special character (!@#…)":  has_special,
        "Not a common password":              no_common,
    }

    if score <= 2:
        label, colour, meter = "Very Weak",   "#f85149", 0.10
    elif score <= 3:
        label, colour, meter = "Weak",        "#ffa657", 0.30
    elif score <= 4:
        label, colour, meter = "Fair",        "#e3b341", 0.55
    elif score <= 5:
        label, colour, meter = "Strong",      "#3fb950", 0.75
    else:
        label, colour, meter = "Very Strong", "#1f6feb", 1.00

    return checks, label, colour, meter, score


# ── Password input ─────────────────────────────────────────────────────────────
# text_area allows spaces inside the password
password = st.text_area(
    "Enter your password",
    placeholder="Type your password here… (spaces allowed)",
    help="Your password is never stored or transmitted.",
    height=80,
)

# Toggle to reveal / hide (text_area already shows text, so hide by default)
hide = st.checkbox("Hide password", value=True)
if hide:
    password = password  # value kept, just not shown again
else:
    st.code(password, language=None)

# ── Analysis output ────────────────────────────────────────────────────────────
if password.strip():
    checks, label, colour, meter, score = analyse(password)

    # Strength label
    st.markdown(
        f"**Strength: <span style='color:{colour}'>{label}</span>** &nbsp;({score}/7 criteria met)",
        unsafe_allow_html=True,
    )

    # Simple progress meter
    st.progress(meter)

    # Criteria checklist
    st.markdown("**Checklist**")
    for criterion, ok in checks.items():
        icon = "✅" if ok else "❌"
        st.markdown(f"{icon} {criterion}")

    # Tips
    failed = [k for k, ok in checks.items() if not ok]
    if failed:
        st.warning("💡 **Improve your password:**\n" + "\n".join(f"- {f}" for f in failed))
    else:
        st.success("🎉 Excellent! Your password meets all security criteria.")

else:
    st.info("👆 Enter a password above to see its strength analysis.")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<p style='text-align:center;color:#484f58;font-size:0.8rem;'>"
    "SecurePass · Passwords are analysed locally and never stored."
    "</p>",
    unsafe_allow_html=True,
)
