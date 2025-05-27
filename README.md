# 🎮 Guess the Number Game - Python Web Version (Flask)

A simple web-based number guessing game built with **Python** and **Flask**. The program randomly selects a number between 1 and 100, and the player must guess it through a web interface.

---

## 🧩 Project Description

- The server picks a random number between 1 and 100 and stores it in the user's session.
- The user submits guesses via a web form.
- The application responds with hints: `"Too high"`, `"Too low"`, or `"Correct!"`.
- The number of attempts is tracked in the session and shown after a correct guess.
- Web-based version using the Flask web framework.

---

## 🛠️ Requirements

Make sure you have Python installed (version 3.6 or above recommended). Then install Flask:

```bash
pip install flask
```

---

## 🚀 How to Run

### 1. Clone project
```bash
git clone https://github.com/egigiffari/guess-number-py.git guess_number_game
```

### 2. RUN project
```bash
cd guess_number_game
```

#### Windows
```bash
python app.py
```

#### Linux/MacOS
```bash
python3 app.py
```
