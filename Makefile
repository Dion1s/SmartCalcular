.PHONY: install run clean build help test

install:
	python -m pip install -r requirements.txt
	python -m pip install pytest pytest-cov

run:
	python src/Tkinter_Calculator.py

clean:
	if exist __pycache__ rmdir /s /q __pycache__
	if exist .pytest_cache rmdir /s /q .pytest_cache
	if exist dist rmdir /s /q dist
	if exist build rmdir /s /q build
	if exist *.egg-info rmdir /s /q *.egg-info

build:
	python -m PyInstaller --onefile --windowed --name SmartCalculator --add-data "imgs/*;imgs/" src/Tkinter_Calculator.py

help:
	@echo Available commands:
	@echo make install - Install dependencies
	@echo make run    - Run the calculator
	@echo make clean  - Clean temporary files
	@echo make build  - Create executable file

test:
	python -m pytest tests/ --cov=src --cov-report=term-missing 