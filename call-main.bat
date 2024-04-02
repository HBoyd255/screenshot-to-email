@echo off
setlocal

rem Activate the virtual environment
call venv\Scripts\activate

rem Run the Python script headlessly
pythonw main.py

rem Deactivate the virtual environment
deactivate

endlocal
