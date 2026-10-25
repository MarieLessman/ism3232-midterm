# ISM3232 Midterm: Brightline Print Shop

- **Name:** Marie Lessman
- **Version:** GAMMA
- **Date:** 10/25/2026

## What This Program Does

This program prices print jobs for Brightline Print Shop. It figures out each job's total after discounts and fees. It decides whether the job needs a printed proof or an overnight press run. Lastly, it prints a report the owner can read. The report ends with summary lines like the total invoiced and the largest job. 

## Business Rules

1. the print cost is the price per copy times the number of copies. 
2. Jobs of 200 to 999 copies get 8% off, and jobs of 1,000 or more get 15% off. 
3. Registered student organizations get 5 extra percentage points off, but only on jobs of 200 copies or more. 
4. If the discounted cost is under $40, a $15 setup fee is added. 
5. A job total over $300 needs a printed proof. 
6. A job needs an overnight press run if it has more than 500 copies or its total is over $400. 

## How to Run

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## How to Test

```
ruff check .
pytest -v
```

There are 20 tests in tests/test_business_rules.py.

## Files in this Repository

- .gitignore: lists files and folders Git should not track, like .venv and __pycache__
- business_rules.py: the eight functions that apply the pricing rules
- commands.md: my terminal record showing how I built and checked the project
- main.py: the job list and the code that prints the report
- README.md: this file, which explains the project
- requirements.txt: the Python packages needed to run and test the project
- tests/__init__.py: an empty file that makes tests a Python package
- tests/test_business_rules.py: the 20 pytest tests for the business rules

## AI Use Statement 

I did not use AI on this exam. 