# OrangeHRM Automation Testing Project

## Overview
Automated UI testing for [https://opensource-demo.orangehrmlive.com](https://opensource-demo.orangehrmlive.com) using Selenium and Pytest in a Page Object Model (POM) structure.

## Objective
Automate login, logout, user management, leave and claim operations using:

Selenium with Python

Page Object Model (POM)

Pytest Framework

Data-driven testing (Excel/CSV)

Explicit waits



## Technologies
- Python
- Selenium
- Pytest
- Webdriver Manager
- Pytest HTML
- openpyxl

## To Run:
```bash
pip install -r requirements.txt

pytest -v -s --capture=sys --html=Reports/OrangeHRM_Automation_reports.html