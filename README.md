# 🔐 SecurePass

A simple cybersecurity project built with **Python** and **Streamlit** that checks the strength of a password in real time.

---

## 📌 Features

- Password input text box (spaces allowed)
- Real-time strength meter — fills up as your password gets stronger
- 7-point checklist to evaluate your password
- Suggestions to improve weak passwords
- Hide / show password toggle
- Passwords are **never stored or transmitted** — everything runs locally

---

## 🔢 Strength Levels

| Level | Score | Colour |
|---|---|---|
| Very Weak | 1 – 2 | 🔴 Red |
| Weak | 3 | 🟠 Orange |
| Fair | 4 | 🟡 Yellow |
| Strong | 5 | 🟢 Green |
| Very Strong | 6 – 7 | 🔵 Blue |

---

## ✅ Password Checklist

The app checks all 7 criteria:

1. At least 8 characters
2. At least 12 characters *(recommended)*
3. Contains an uppercase letter (A-Z)
4. Contains a lowercase letter (a-z)
5. Contains a digit (0-9)
6. Contains a special character (`!@#$%^&*` etc.)
7. Not a common password (`password`, `123456`, `qwerty`…)

---

## 🗂️ Project Structure

```
secure_pass/
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

---

## ⚙️ Requirements

- Python 3.8 or higher
- Streamlit 1.32 or higher

---

## 🚀 How to Run

**Step 1 — Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 2 — Start the app**

```bash
python -m streamlit run app.py
```

**Step 3 — Open in browser**

```
http://localhost:8501
```

> If the browser does not open automatically, paste the URL above into any browser.

**To stop the app:** press `Ctrl + C` in the terminal.

---

## 🛡️ Privacy

All password analysis happens **locally in your browser session**.  
No data is sent to any server, saved to a file, or logged anywhere.

---

## 🧰 Built With

- [Python](https://www.python.org/) — core logic
- [Streamlit](https://streamlit.io/) — web UI framework
