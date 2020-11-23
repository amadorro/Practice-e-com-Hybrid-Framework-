REM chrome
REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

REM firefox
REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser firefox
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox

REM pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser 
REM pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser 
REM pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser 
