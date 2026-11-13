# NUMBER-MYSTERY-
python based puzzle game that challenges player to deduce a hidden secret code within limited attempts

# 🧠 Number Mystery Game

## 📌 Project Description

Number Mystery is a simple and interactive number guessing game developed using Python.

In this game, the computer generates a secret 4-digit number, and the player must guess the correct number within 10 attempts.

The game provides clues after every incorrect guess to help the player discover the secret code.

## 🎯 Objectives

- Develop logical thinking and problem-solving skills.
- Understand Python programming concepts.
- Practice loops, conditions, functions, and random number generation.
- Create an interactive console-based game.

## 🛠️ Technologies Used

- Programming Language: Python
- Module: Random
- Interface: Command Line / Terminal

## 🎮 Game Rules

1. The computer generates a random 4-digit secret number.
2. All digits in the secret number are different.
3. The first digit cannot be zero.
4. The player has 10 attempts to guess the secret number.
5. The player receives clues after each incorrect guess.
6. The player wins by guessing the correct number.

## 💡 Clue System

| Symbol | Meaning |
|---|---|
| 🟢 | Correct digit in the correct position |
| 🟡 | Correct digit in the wrong position |
| 🔴 | Digit is not in the secret number |

## ✨ Features

- Random 4-digit number generation.
- 10 guessing attempts.
- Score tracking system.
- Instant feedback and hints.
- Input validation.
- Win and Game Over messages.
- Simple and user-friendly interface.

## 📂 Project Structure

```text
Number-Mystery-Game/
│
├── number_mystery.py
│
└── README.md
```

## ⚙️ Installation

### Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

### Step 2: Download the Project

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Or download the project files.

### Step 3: Open the Project Folder

```bash
cd Number-Mystery-Game
```

### Step 4: Run the Program

```bash
python number_mystery.py
```

No additional packages are required because the game uses Python's built-in random module.

## 🖥️ Sample Output

```text
=============================================
       NUMBER MYSTERY GAME
=============================================

Welcome to the Secret Code Challenge!
Find the hidden 4-digit number.
All digits are different.
You have 10 attempts.

CLUES:
Correct digit and correct position
Correct digit but wrong position
Digit is not in the secret number

Attempts remaining: 10
Current score: 100

Enter your 4-digit guess: 1234

Your clues:
Correct position: 1
Wrong position: 2
Not in code: 1
```

*Note: Actual clues will vary because the secret number is randomly generated.*

## 🧠 Python Concepts Used

- `import random` – Generates random numbers.
- `random.sample()` – Selects unique digits.
- `while` loop – Repeats the game.
- `if-else` statements – Checks conditions.
- `for` loop – Compares individual digits.
- `input()` – Accepts player guesses.
- `print()` – Displays game instructions and results.
- `len()` and `set()` – Validate the player's input.

## 🚀 Future Enhancements

- Add Easy, Medium, and Hard difficulty levels.
- Create a graphical user interface using Tkinter or Pygame.
- Add sound effects and background music.
- Save player names and high scores.
- Add a leaderboard.
- Provide additional mystery hints.

## 👨‍💻 Author

**Project Name:** Number Mystery Game

**Language:** Python

**Project Type:** Mini Project

## 📜 License

This project is created for educational and learning purposes.

---

⭐ If you like this project, give it a star on GitHub!
