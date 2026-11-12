Fake python job listings web sraper
===

This project scrape website from [Fake Python](https://realpython.github.io/fake-jobs/). 
The result is a csv file include 4 information: Job title, company name, location, job detail page url.
# How to start
Python: 3.14+

Step 1: Create virtual environment (Optional)
```
python -m venv website-scrape

# Command prompt
./website-scrape/Scripts/activate.bat

# Powershell
./website-scrape/Scripts/Activate.ps1
```

Step 2: Install libraries
```
pip install -r requirements.txt
```

Step 3: Run program
```
python -m main.py
```