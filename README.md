# Practice-e-com-Hybrid-Framework-
Practice (e-com Hybrid-Framework) with regression and sanity test

Practice (e-com Hybrid-Framework) with regression and sanity test 
Note: Loggings will be generated when the html reports are generated

Install the following on pycharm:
Selenium - Library 
Pytest - Python UnitTest framework
pytest-hmtl - Pytest HTML Reports 
pytest-xdist - Run tests parallel 
Openpyxl - MS Excel support 
Allure-pytest - To generate allure reports 

These required python packages:
pageObjects, testCases, and utilities.
The rest are regular directories

Run the test using pycharm terminal:
pytest -s -v --html:Reports\report.html testCases/test_login.py --browser chrome
