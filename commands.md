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

## 3. The project structure

## 4. Every function and test

## 5. Which files print

## 6. The commit history 

