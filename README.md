# Tic-Tac-Toe
AI-powered Tic-Tac-Toe game built with Python and Tkinter, featuring an unbeatable Minimax Algorithm for optimal decision-making.

## Overview

This project is a Python-based Tic-Tac-Toe game with a graphical user interface (GUI) built using Tkinter. The game allows a human player to compete against an AI opponent that uses the Minimax algorithm to make optimal decisions.

The AI evaluates all possible future game states and selects the best move, making it impossible to defeat when played correctly.

---

## Features

* Interactive graphical interface using Tkinter
* Human vs AI gameplay
* Unbeatable AI powered by the Minimax algorithm
* Automatic win, loss, and draw detection
* Game reset functionality
* Clean and simple code structure

---

## Project Structure

```text
project/
│
├── tictactoe_logic.py    # Game logic and AI implementation
├── tic_tac_toi_gui.py    # Tkinter graphical interface
└── README.md             # Project documentation
```

---

## Technologies Used

* Python 3
* Tkinter (GUI)
* Minimax Algorithm
* Object-Oriented Programming (OOP)

---

## How the Project Works

### 1. Game Board

The game board is represented as a list containing 9 positions:

```python
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
```

Board Layout:

```text
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
```

---

### 2. Game Logic

The logic file handles:

* Board creation
* Win detection
* Draw detection
* Game-over conditions
* AI move calculation

Important functions:

* `create_board()`
* `check_win()`
* `check_draw()`
* `evaluate()`
* `minimax()`
* `find_best_move()`

---

### 3. GUI

The graphical interface is built using Tkinter.

The GUI handles:

* Displaying the board
* User interactions
* Updating game status
* Displaying results
* Resetting the game

---

## AI Implementation

The AI uses the Minimax algorithm.

### How Minimax Works

The algorithm:

1. Simulates every possible move.
2. Predicts all future responses from the opponent.
3. Evaluates each possible game outcome.
4. Selects the move with the highest score.

Scoring System:

| Outcome    | Score |
| ---------- | ----- |
| AI Wins    | +10   |
| Human Wins | -10   |
| Draw       | 0     |

Depth is also considered to:

* Prefer faster wins
* Delay losses as much as possible

---

## Workflow

```text
Human Move
     ↓
Board Updated
     ↓
Check Win/Draw
     ↓
AI Calculates Best Move
     ↓
Minimax Evaluation
     ↓
Best Move Selected
     ↓
Board Updated
     ↓
Repeat Until Game Ends
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/MuhammadAli133/Tic-Tac-Toe.git
```

### Navigate to Project Folder

```bash
cd TIC TAC TOE
```

### Run the Application

```bash
python tic_tac_toi_gui.py
```
make sure the python 3 is insatlled on your system before using it.
---

## Learning Objectives

This project demonstrates:

* Python programming fundamentals
* GUI development using Tkinter
* Artificial Intelligence concepts
* Minimax algorithm implementation
* Recursive programming
* Game development fundamentals

---

## Future Improvements

Possible enhancements include:

* Difficulty levels (Easy, Medium, Hard)
* Alpha-Beta Pruning optimization
* Score tracking system
* Player vs Player mode
* Improved UI design
* Sound effects and animations
* Online multiplayer support

---

## Author

Developed as an educational project to demonstrate Artificial Intelligence concepts through a Tic-Tac-Toe game.

---

## License

This project is open-source and available for educational and learning purposes.
