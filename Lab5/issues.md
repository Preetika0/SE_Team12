
# Lab 5 – Static Code Analysis

## Issue Identification and Resolution

The scholarship disbursement program was analyzed using Pylint, Bandit, and Flake8 to identify security vulnerabilities, programming errors, and code quality issues.

### Identified Issues

| No. | Issue | Tool | Type / Severity | Original Line | Description | Fix Approach |
|---|---|---|---|---|---|---|
| 1 | SQL Injection (B608) | Bandit | Security – Medium | 10 | SQL query used string formatting to insert user inputs directly into the query. | Replaced string formatting with parameterized SQL queries using placeholders. |
| 2 | Mutable Default Argument (W0102) | Pylint | Bug | 9 | The default argument `audit=[]` shared the same list across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| 3 | Insecure Shell Execution (B605) | Bandit | Security – Low | 26 | `os.system()` executed a shell command to display an archive message. | Removed shell execution and replaced it with a Python print statement. |
| 4 | Partial Executable Path (B607) | Bandit | Security – Low | 26 | The program executed a shell command through a partial executable path. | Removed the external shell command entirely. |
| 5 | Silent Exception Handling (B110) | Bandit | Code Quality – Low | 27–28 | A broad exception was caught and ignored using `pass`. | Removed unnecessary exception handling along with the shell command. |
| 6 | Broad Exception Handling (W0718) | Pylint | Code Quality | 27 | The program caught the general `Exception` class instead of handling specific errors. | Removed the unnecessary try-except block. |
| 7 | Global Variable Usage (W0603) | Pylint | Code Quality | 15–16 | The `disburse()` function modified a global variable. | Removed global state and calculated the disbursed total locally in `main()`. |
| 8 | Incorrect None Comparison (E711) | Flake8 / Pylint | Style | 32 | The program used `scheme == None` instead of the recommended identity comparison. | Changed it to `scheme is None`. |
| 9 | Incorrect Function Naming (C0103) | Pylint | Code Quality | 31 | The function `bySchemeCount()` did not follow snake_case naming conventions. | Renamed it to `by_scheme_count()`. |
| 10 | Long Lines (E501) | Flake8 | Style | 5, 10, 17, 19, 34 | Several lines exceeded the recommended 79-character limit. | Split long statements and formatted SQL queries across multiple lines. |
| 11 | Missing Docstrings (C0114, C0116) | Pylint | Code Quality | Multiple | The module and functions did not have documentation strings. | Added module-level and function-level docstrings. |

### Verification Results

| Tool | Before Fixing | After Fixing |
|---|---|---|
| Pylint | 5.00/10 | 10.00/10 |
| Bandit | 1 Medium, 3 Low findings | No issues identified |
| Flake8 | 6 violations | No violations |

### Conclusion

Static analysis helped identify security vulnerabilities, programming errors, and formatting problems in the scholarship disbursement program. After applying the necessary corrections, the program achieved a Pylint score of 10/10, with no remaining Bandit security findings or Flake8 violations.
