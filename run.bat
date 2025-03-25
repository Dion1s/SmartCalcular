@echo off
if "%1"=="install" goto install
if "%1"=="run" goto run
if "%1"=="clean" goto clean
if "%1"=="build" goto build
if "%1"=="test" goto test
goto help

:install
echo Installing dependencies...
python -m pip install -r requirements.txt
python -m pip install pytest pytest-cov
goto end

:test
echo Running tests...
set PYTHONPATH=%CD%
python -m pytest tests/ --cov=src --cov-report=term-missing
goto end

:run
echo Starting calculator...
python src/Tkinter_Calculator.py
goto end

:clean
echo Cleaning temporary files...
if exist __pycache__ rmdir /s /q __pycache__
if exist .pytest_cache rmdir /s /q .pytest_cache
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.egg-info rmdir /s /q *.egg-info
goto end

:build
echo Creating executable...
python -m PyInstaller --onefile --noconsole --clean --windowed --name SmartCalculator --add-data "imgs/*;imgs/" src/Tkinter_Calculator.py
echo Build completed. Check the dist folder.
goto end

:help
echo Available commands:
echo run.bat install - Install dependencies
echo run.bat run    - Run the calculator
echo run.bat clean  - Clean temporary files
echo run.bat build  - Create executable file
echo run.bat test   - Run tests with coverage report

:end 