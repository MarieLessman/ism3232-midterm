# Terminal Record: Brightline Print Shop

## 1. Building the project
cd ~
pwd
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
echo ".venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
pip freeze > requirements.txt
ls -la
ls
git status 
git add . 
git commit -m "set up for midterm project structure, gitignore, and requirements"
git remote add origin https://github.com/MarieLessman/ism3232-midterm.git
git push -u origin main

## 2. The virtual environment
```
which python3
```

```
/Users/marie/ism3232-midterm/.venv/bin/python3
```

The path shows python3 inside the .venv folder in my project, not the system Python, which shows the virtual environment is active.

## 3. The project structure
```
tree -L 2
```

```
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The .venv folder is on my computer but not in my Github repository because it's listed in .gitignore since it is large and specific to my machine. 

## 4. Every function and test
```
rg 'def '
```

```
business_rules.py
25:def calculate_print_cost(copy_price: float, copies: int) -> float:
29:def get_volume_discount(copies: int, student_org: bool = False) -> float:
43:def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
54:def requires_proof(total: float) -> bool:
58:def needs_overnight_run(copies: int, total: float) -> bool:
62:def total_invoiced(jobs: list) -> float:
71:def largest_job(jobs: list) -> str:
84:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

tests/test_business_rules.py
13:def test_print_cost_multiples_price_and_copies():
16:def test_discount_199_copies_has_no_discount():
19:def test_discount_200_copies_is_8_percent():
22:def test_discount_999_copies_is_8_percent():
25:def test_discount_1000_copies_is_15_percent():
28:def test_job_total_at_40_dollars_has_no_setup_fee():
31:def test_job_total_just_below_40_dollars_adds_setup_fee():
34:def test_job_total_changes_when_student_org_is_true():
40:def test_proof_not_required_at_300_dollars():
43:def test_proof_required_just_over_300_dollars():
46:def test_overnight_not_needed_at_500_copies():
49:def test_overnight_needed_at_501_copies():
52:def test_overnight_not_needed_at_400_dollars():
55:def test_overnight_needed_just_over_400_dollars():
58:def test_total_invoiced_adds_up_all_jobs():
65:def test_largest_job_returns_title_with_biggest_total():
74:def test_largest_job_tie_returns_first_in_list():
82:def test_largest_job_empty_list_returns_empty_string():
86:def test_format_job_line_with_both_flags_yes():
92:def test_format_job_line_rounds_to_two_decimals():
```

business_rules.py defines 8 functions and tests/test_business_rules.py defines 20 tests.

## 5. Which files print
```
rg -l 'print'
```

```
tests/test_business_rules.py
commands.md
business_rules.py
main.py
```

main.py is the only Python file that prints, since it calls print(). business_rules.py appears in the list only because "print" is part of the function name calculate_print_cost, and it never calls print() because its functions return values and main.py does the printing. 

## 6. The commit history 
```
git log --oneline
```

```
394d860 (HEAD -> main, origin/main) add tests for total_invoiced, largest_job, and format_job_line
1f574b4 add tests for proof and overnight run limits
da15698 add tests for setup fee limit and student org discount
4d9054d add tests for print cost and discount tiers
bde8e84 Fix counter indent so counts run inside the loop
72148f3 Add summary lines to job report
2b681dd Add imports, job lists, and job report loop with per-job lines and counters
2e2f811 Add all eight business_rules functions
e6f4545 added section 1 building the project
86ca5e3 remove .DS_Store and add it to gitignore
b9cc825 set up for midterm project structure, gitignore, and requirements
```

There are 11 commits at this point. 


