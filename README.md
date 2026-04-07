![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![100 Days of Code](https://img.shields.io/badge/100DaysOfCode-Day%2012-orange)

# 🎯 Number Guessing Game
A simple Python console game where the player tries to guess a randomly generated number between 1 and 100. The game includes two difficulty modes and gives feedback after each guess.

## 💡 What I Learned
- Structuring a simple game loop using a **while loop**
- Breaking logic into **clear, reusable functions**
- Using **input validation** to prevent crashes
- Applying **conditional logic** to give meaningful feedback (too high / too low)
- Managing game difficulty by adjusting **attempt limits**
- Improving readability with **docstrings**, comments, and clean function names
- Designing a small project with a **modular, beginner‑friendly structure**

## 🧠 How It Works
1. The game generates a secret number between **1 and 100**.
2. The player chooses a difficulty level:
   - **Easy** → 10 attempts  
   - **Hard** → 5 attempts
3. The player enters a guess each round.
4. The game provides feedback:
   - **Too high**
   - **Too low**
   - **Correct!**
5. After each incorrect guess, the number of remaining attempts decreases.
6. The game ends when the player:
   - Guesses the number correctly, or  
   - Runs out of attempts

## 🏆 Example Output
```
You have 9 attempts remaining.
Make a guess: 72
Too high.
Guess again.

You have 8 attempts remaining.
Make a guess: 63
You got it! The answer was 63.
```

## 🚀 How to Play
Run `main.py` in a Python environment and follow the prompts:

## 📁 Files
- `main.py`: Main game logic
- `art.py`: Contains ASCII art logo

## 📚 Credits
Art inspired by the [100 Days of Code: Python Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. Used for educational purposes under fair use.

## 🙏 Acknowledgements
- Thanks to Dr. Angela Yu and the team behind the 100 Days of Code: Python Bootcamp for the original project structure and assets.
- This version was adapted and expanded by me as part of my creative developer-educator journey.
- Built with care to reinforce beginner-friendly logic and clean game design.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
