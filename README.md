# Python Bootcamp - Module 01 (Basics 2)

This repository contains exercises from **Module 01 – Basics 2** of the Python Bootcamp.  
The goal of this module is to get familiar with **Object-Oriented Programming (OOP)**, built-in Python methods, generators, and class manipulation.

---

## Prerequisites

- Python **3.7** or higher  
  Check your Python version:
  ```bash
  python -V
  ```
- Optional: `pycodestyle` to check PEP 8 code style:
  ```bash
  pip install pycodestyle
  ```

> **Note:** The `eval()` function is **not allowed**.

---

## Exercises Overview

| Chapter | Exercise | File(s) | Objective |
|---------|---------|---------|-----------|
| II | 00 – The Book | `book.py`, `recipe.py`, `test.py` | Learn class creation and object manipulation. Implement `Book` and `Recipe` classes with validation and printing. |
| III | 01 – Family Tree | `game.py` | Practice class inheritance. Implement parent `GotCharacter` and child house classes like `Stark`. Methods: `print_house_words()`, `die()`. |
| IV | 02 – The Vector | `vector.py`, `test.py` | Work with vectors using lists (no NumPy). Implement operations: addition, subtraction, scalar multiplication/division, dot product, transpose, and magic methods. |
| V | 03 – Generator | `generator.py` | Learn generator objects. Implement `generator(text, sep=" ", option=None)` with options: `shuffle`, `unique`, `ordered`. Handle errors. |
| VI | 04 – Working with Lists | `eval.py` | Explore `zip` and `enumerate`. Implement `Evaluator` class with static methods `zip_evaluate` and `enumerate_evaluate` for weighted word length sums. |
| VII | 05 – Bank Account | `the_bank.py` | Implement `Bank` class to handle `Account` objects securely. Methods: `add(account)`, `transfer(origin, dest, amount)`, `fix_account(name)`. Validate accounts and handle corrupted ones. |

---

## How to Run Exercises

1. Navigate to the folder containing the exercise files:
```bash
cd path/to/exercise/folder
```

2. Run the test script for the exercise:
```bash
python3 test.py           # For Book, Recipe, or Vector exercises
python3 test_bank.py      # For Bank Account exercise
```

3. Check the output to ensure your code works as expected.

---

## Notes

- Test your code with different cases to handle errors correctly.  
- Follow meaningful naming conventions for variables and functions.  
- Use the official Python documentation for guidance.  
- Peer collaboration and discussion on Discord (for 42 students) is encouraged.  

---

## Acknowledgements

This bootcamp was developed and supervised by the 42AI team:

- Maxime Choulika, Pierre Peigné, Matthieu David, Quentin Feuillade–Montixi, Mathieu Perez  
- Louis Develle, Augustin Lopez, Luc Lenotre, Owen Roberts, Thomas Flahault, Amric Trudel, Baptiste Lefeuvre, Mathilde Boivin, Tristan Duquesne  

Licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International**.
