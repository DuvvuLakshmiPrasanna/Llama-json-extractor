@echo off
REM Quick setup script for Windows

echo.
echo ========================================
echo  Invoice JSON Extractor - Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

echo [1/3] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo [2/3] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ========================================
echo  ✅ Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Place your model in ./model folder
echo 2. Run: python app.py
echo 3. Open: http://127.0.0.1:7860
echo.
echo For deployment, see: DEPLOYMENT.md
echo.
pause
