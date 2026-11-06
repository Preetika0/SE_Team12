# Lab 5 – Static Code Analysis

## 1. Objective

The objective of this lab is to improve Python code quality, security, and maintainability using three static code analysis tools:

- **Pylint** – Identifies programming errors, code quality issues, and potential bugs.
- **Bandit** – Detects common security vulnerabilities in Python code.
- **Flake8** – Checks Python code formatting and adherence to PEP 8 guidelines.

## 2. Project Description

The assigned project is a Scholarship Disbursement Ledger developed using Python and SQLite.

The program provides functionality to:
- Grant scholarships to students.
- Store scholarship details in an SQLite database.
- Disburse scholarship amounts.
- Count awards based on scholarship schemes.
- Archive scholarship records.

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Python | Programming language |
| SQLite | Database management |
| Pylint | Code quality analysis |
| Bandit | Security vulnerability detection |
| Flake8 | Code style and formatting analysis |
| VS Code | Development environment |

## 4. Issues Identified and Fixed

The original program was analyzed using Pylint, Bandit, and Flake8.

The major issues identified included:

1. SQL injection vulnerability due to string-based SQL query construction.
2. Mutable default argument in the scholarship grant function.
3. Insecure shell command execution using `os.system()`.
4. Silent exception handling using `except` and `pass`.
5. Unnecessary global variable usage.
6. Incorrect comparison with `None`.
7. Function naming convention violations.
8. Missing module and function docstrings.
9. Long lines violating PEP 8 guidelines.

These issues were addressed by implementing parameterized SQL queries, correcting default arguments, removing shell execution, improving exception handling, and following Python naming and formatting conventions.

Detailed findings and corrections are documented in [issues.md](issues.md).

## 5. Static Analysis Results

The tools were executed before and after modifying the program.

| Tool | Before Fixing | After Fixing |
|---|---|---|
| Pylint | 5.00/10 | 10.00/10 |
| Bandit | 4 findings | 0 findings |
| Flake8 | 6 violations | 0 violations |

## 6. Project Structure

```text
Lab5/
│
├── scholarship_disbursement.py
├── issues.md
├── README.md
├── .gitignore
│
├── pylint_before.txt
├── pylint_after.txt
│
├── bandit_before.txt
├── bandit_after.txt
│
├── flake8_before.txt
└── flake8_after.txt
```

## 7. How to Run the Project

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install the required tools

```bash
pip install pylint bandit flake8
```

### Step 4: Execute the program

```bash
python scholarship_disbursement.py
```

### Step 5: Run static analysis

**Pylint**

```bash
pylint scholarship_disbursement.py
```

**Bandit**

```bash
bandit -r scholarship_disbursement.py
```

**Flake8**

```bash
flake8 scholarship_disbursement.py
```

## 8. Conclusion

This lab demonstrated the importance of static code analysis in identifying security vulnerabilities, programming errors, and code formatting issues without executing the source code during analysis.

After applying the necessary corrections, the program achieved a Pylint score of 10/10, with zero issues reported by Bandit and zero violations reported by Flake8.

The exercise improved the security, readability, maintainability, and overall quality of the scholarship disbursement program.
