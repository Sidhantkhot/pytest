rem chrome
rem pytest -v -m regression  --browser chrome --html=Reports\report.html testCases
rem pytest -v -m sanity  --browser chrome --html=Reports\report.html testCases

rem firefox

pytest -v -m sanity --browser ff --html=Reports\report.html testCases