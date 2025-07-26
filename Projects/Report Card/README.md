#  Student Report Card Generator

This is a simple Python program that generates student report cards by:
- Taking student names and their grades as input
- Calculating average grades
- Identifying the best and worst students
- Reporting whether each student passed or failed

---

##  How It Works

1. The user enters the total number of students.
2. For each student:
   - A valid name is entered (non-empty, no numbers)
   - A list of grades is entered (separated by commas, each between 0–100)
3. The program calculates each student's average.
4. It prints:
   - The best and worst performing students
   - A pass/fail result for every student

---

##  Features

- Input validation for number of students, names, and grades
- Calculates and displays averages with 1 decimal precision
- Automatically sorts students by performance
- Marks students as **Pass** (average ≥ 60) or **Fail** (average < 60)

---

##  Requirements

- Python 3.6+

No third-party libraries are required.

---

##  How to Run

1. Clone or download the repository
2. Open a terminal and navigate to the project folder
3. Run the Python file:
```bash
python report_card.py
