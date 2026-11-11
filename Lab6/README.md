# Lab 6 – Code and Branch Coverage Analysis

## Application
`food_delivery.py` is the assigned food-delivery application. It calculates delivery charges, applies coupons, and estimates delivery time.

## Deliverables
- `CodeCoverageTest_food_delivery_application.py` – tests designed to execute all application statements.
- `BranchCoverageTest_food_delivery_application.py` – tests designed to exercise both outcomes of decision branches.
- `screenshots/` – add the terminal screenshots from your own test runs.

## Setup (Windows PowerShell)
Run these commands from this `Lab6` directory:

```powershell
py -m pip install pytest coverage
```

## 1. Code coverage run
```powershell
coverage erase
coverage run --source=food_delivery -m pytest -q CodeCoverageTest_food_delivery_application.py
coverage report -m
```

## 2. Branch coverage run
```powershell
coverage erase
coverage run --branch --source=food_delivery -m pytest -q BranchCoverageTest_food_delivery_application.py
coverage report -m
```

The `--source=food_delivery` option ensures the report measures the application module rather than pytest or the test files. The branch run uses `--branch` to measure decision outcomes as well as executed lines.

## Screenshots
Save the successful terminal output as:
- `screenshots/code_coverage.png`
- `screenshots/branch_coverage.png`

Capture the complete terminal section showing the pytest result and the `coverage report -m` table. Do not submit screenshots until the run succeeds on your machine.

## Analysis
Code/statement coverage checks whether executable statements were run. Branch coverage additionally checks whether each decision outcome (for example, True and False for an `if`) was exercised. A test suite can execute every statement while still missing an alternate decision outcome; therefore, branch coverage is a stricter measure.

## Important
The two reports are separate runs. Keep the code-coverage test file and its first Git commit separate from the branch-coverage test file and its second Git commit, as required by the lab handout.
