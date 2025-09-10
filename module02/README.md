# Python Bootcamp - Module 02 (Basics 3)

This repository contains exercises from **Module 02 – Basics 3** of the Python Bootcamp.  
The goal of this module is to practice **decorators, lambda, context managers, packaging, and basic statistics**.

---

## 📌 Prerequisites
- **Python 3.7** or higher  
  Check your version:
  ```bash
  python -V
  ```
- Optional: [pycodestyle](https://pypi.org/project/pycodestyle/) to check PEP 8 style:
  ```bash
  pip install pycodestyle
  ```
- ⚠️ **The `eval()` function is forbidden** in all exercises.

---

## 📂 Exercises Overview

| Chapter | Exercise | File(s) | Objective |
|---------|----------|---------|-----------|
| II | 00 – Map, Filter, Reduce | `ft_map.py`, `ft_filter.py`, `ft_reduce.py` | Reimplement Python’s built-in `map`, `filter`, and `reduce` using generators. |
| III | 01 – Args and Kwargs | `main.py` | Practice `*args` and `**kwargs` to dynamically create attributes in an object (`ObjectC`). |
| IV | 02 – The Logger | `logger.py` | Implement a `@log` decorator that writes execution details (function name, time, username) into `machine.log`. |
| V | 03 – CSV Reader | `csvreader.py` | Create a `CsvReader` class as a **context manager** to handle CSV files, with error detection (bad formatting, inconsistent records). |
| VI | 04 – MiniPack | `build.sh`, `my_minipack/` (modules, configs, docs) | Package your own Python library containing: a progress bar and the logger. Learn how to build, install, and check a package with `pip`. |
| VII | 05 – TinyStatistician | `TinyStatistician.py` | Implement basic statistical methods (`mean`, `median`, `quartiles`, `var`, `std`) **without using built-in stats functions**. |

---

## ▶️ How to Run the Exercises

Navigate to the folder containing the exercise files:

```bash
cd path/to/module02/exercise/folder
```

Run the Python scripts:

```bash
# Map, Filter, Reduce
python3 ft_map.py

# Args and Kwargs
python3 main.py

# Logger
python3 logger.py

# CSV Reader
python3 csvreader.py

# MiniPack (build & install)
bash build.sh
pip install ./dist/my_minipack-1.0.0.tar.gz

# TinyStatistician
python3 TinyStatistician.py
```

---

## 📝 Notes
- Always test your code with **different edge cases** (empty lists, bad inputs, invalid options, corrupted files).
- Follow **PEP 8** conventions for clean, readable code.
- Use Python’s official documentation to learn more about **decorators, context managers, packaging, and statistics**.
- For 42 students: you can discuss solutions on the **Discord Bootcamp channel**.

---

## 🙌 Acknowledgements
This module is part of the **42AI Python Bootcamp**, created and supervised by:

- Maxime Choulika, Pierre Peigné, Matthieu David, Quentin Feuillade–Montixi, Mathieu Perez  
- Louis Develle, Augustin Lopez, Luc Lenotre, Owen Roberts, Thomas Flahault  
- Amric Trudel, Baptiste Lefeuvre, Mathilde Boivin, Tristan Duquesne  

Licensed under **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International**.  
