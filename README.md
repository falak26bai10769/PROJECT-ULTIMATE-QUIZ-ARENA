# Ultimate Quiz Arena

## Project Description

Ultimate Quiz Arena is an interactive command-line Python quiz game designed to combine learning, competition, and entertainment. The project provides multiple subjects, difficulty levels, game modes, power-ups, mini-games, achievements, XP, coins, player statistics, and a session-based leaderboard.

The project demonstrates important Python programming concepts such as functions, loops, conditional statements, dictionaries, lists, input handling, randomization, time-based features, calculations, and data processing.

---

## Features

### 1. Multiple Subjects

The quiz includes four main subjects:

* Python
* Mathematics
* Science
* General Knowledge

Each subject contains questions across different difficulty levels.

### 2. Difficulty Levels

Questions are divided into:

* Easy
* Medium
* Hard

The difficulty level affects scoring and the challenge of the quiz.

### 3. Game Modes

The project provides several ways to play:

* **Classic Quiz** – Play a standard quiz based on a selected subject and difficulty.
* **Rapid Fire** – Answer a shorter set of questions with faster gameplay.
* **Survival Mode** – Continue answering questions while managing limited lives.
* **Risk & Reward** – Choose between safe and higher-risk scoring options.
* **Boss Battle** – Face a difficult challenge and earn bonus rewards.
* **Daily Challenge** – Complete a special challenge once during the session.
* **Tournament** – Progress through Qualifier, Semi-Final, and Final rounds.
* **Category Mix** – Answer questions from different subjects and difficulty levels.
* **Game Hub** – Play additional mini-games.

### 4. Power-Ups and Lifelines

Players can use different power-ups to improve their chances:

* 50/50
* Hint
* Phone a Friend
* Skip
* Double Points
* Shield

Power-ups have limited availability and can also be obtained through the Arena Shop.

### 5. XP and Level System

Players earn XP while playing.

As XP increases, the player's level can increase. Level progression also provides additional coin rewards.

### 6. Coins and Arena Shop

Coins can be earned through gameplay and used in the Arena Shop to purchase additional power-ups.

### 7. Streak System

The game tracks:

* Current streak
* Best streak
* Correct answers
* Wrong answers
* Questions answered

Streaks can also affect scoring and achievements.

### 8. Achievements

The game contains multiple achievements based on player performance.

Examples include:

* First Quiz
* Knowledge Seeker
* Hot Streak
* Quiz Regular
* Boss Winner
* Game Player
* Perfect Round
* Coin Collector
* Tournament Champion
* Streak Master
* Century Club
* Accuracy Ace
* Arena Legend
* All-Rounder

### 9. Mini-Games

The Game Hub includes:

* Quick Math
* Number Hunt
* Rock Paper Scissors

These provide additional ways to earn points and enjoy the game outside the main quiz.

### 10. Performance Lab

The Performance Lab provides statistics about the player's performance, including:

* Accuracy
* Questions answered
* Correct answers
* Wrong answers
* Best streak
* Average answer time
* Fastest answer
* Perfect rounds
* Boss wins
* Tournament wins
* Overall performance classification

### 11. Player Profile

The Player Profile displays important player information such as:

* Score
* XP
* Level
* Coins
* Accuracy
* Streak
* Quizzes played
* Boss wins
* Tournament wins
* Mini-games played
* Achievements
* Power-up inventory

### 12. Session Leaderboard

The project includes a leaderboard that ranks players according to their scores.

The leaderboard works during the current program session. Scores are stored in memory and are not permanently saved after the program closes.

---

## Technologies Used

* Python 3
* `random` module
* `time` module

The project uses Python's standard library and does not require external packages.

---

## Requirements

Before running the project, make sure you have:

* Python 3.x installed
* A computer with a terminal or command prompt
* The project Python file

No additional Python libraries need to be installed.

---

## Installation and Setup

### Step 1: Install Python

Download and install Python 3.x if it is not already installed.

During installation, make sure Python is added to the system PATH.

### Step 2: Download the Project

Download or clone this GitHub repository to your computer.

### Step 3: Open the Project Folder

Open Command Prompt or Terminal and navigate to the folder containing the project.

For example:

```bash
cd path/to/your/project
```

### Step 4: Run the Project

Run the following command:

```bash
python "PROJECT-ULTIMATE QUIZ ARENA.py"
```

If your Python installation uses `python3`, use:

```bash
python3 "PROJECT-ULTIMATE QUIZ ARENA.py"
```

---

## How to Play

### Step 1: Start the Program

Run the Python file from the terminal.

### Step 2: Enter Player Name

The game will ask you to enter your player name.

### Step 3: Open the Main Menu

After entering your name, the main menu provides access to the different game features.

### Step 4: Select a Game Mode

Choose a mode such as:

* Classic Quiz
* Rapid Fire
* Survival Mode
* Risk & Reward
* Boss Battle
* Daily Challenge
* Tournament
* Category Mix
* Game Hub

### Step 5: Answer Questions

For multiple-choice questions, enter:

```text
A
B
C
D
```

The game also allows the player to use available power-ups through the lifeline option.

### Step 6: Earn Rewards

Correct answers can provide:

* Score
* XP
* Coins
* Streak progress
* Achievements

### Step 7: Check Your Performance

Use the Player Profile and Performance Lab to view your progress and statistics.

---

## Main Menu

The project provides the following main menu options:

```text
1. Classic Quiz
2. Rapid Fire
3. Survival Mode
4. Risk & Reward
5. Boss Battle
6. Daily Challenge
7. Tournament
8. Category Mix
9. Game Hub
10. Arena Shop
11. Player Profile
12. Performance Lab
13. Achievements
14. Leaderboard
15. Arena Guide
16. Exit
```

---

## Project Structure

```text
Ultimate-Quiz-Arena/
│
├── PROJECT-ULTIMATE QUIZ ARENA.py
└── README.md
```

### `PROJECT-ULTIMATE QUIZ ARENA.py`

Contains the complete Python implementation of the quiz game, including the question bank, game modes, scoring system, power-ups, achievements, mini-games, player statistics, shop, and leaderboard.

### `README.md`

Contains the project description, features, requirements, setup instructions, and usage instructions.

---

## Python Concepts Demonstrated

This project demonstrates several Python concepts, including:

* Variables
* Data types
* Lists
* Dictionaries
* Tuples
* Functions
* Conditional statements
* `if`, `elif`, and `else`
* `for` and `while` loops
* User input
* Input validation
* Exception handling
* Random number generation
* Time-based calculations
* String formatting
* List comprehensions
* Sorting
* Functions with parameters and return values
* Program control using `if __name__ == "__main__"`

---

## Data Storage

The project does not use a database or permanent file storage.

Player information, scores, achievements, XP, coins, and leaderboard information are maintained during the current execution of the program.

When the program is closed, the session data is cleared.

---

## Future Enhancements

Possible future improvements include:

* Permanent leaderboard storage
* Database integration
* More subjects and question categories
* Larger question banks
* User accounts and profiles
* Graphical user interface
* Online multiplayer mode
* Online leaderboard
* More mini-games
* Additional achievements and rewards

---

## Conclusion

Ultimate Quiz Arena combines educational quizzes with game-based features to create an interactive learning experience. It demonstrates how core Python concepts can be combined to build a complete command-line application with multiple systems such as scoring, levels, achievements, power-ups, mini-games, and performance tracking.

The project focuses on making learning more engaging while providing practical implementation of Python programming concepts.
