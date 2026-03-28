#!/bin/bash

# Quick setup script for macOS/Linux

echo ""
echo "========================================"
echo "  Invoice JSON Extractor - Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.10+ from https://python.org"
    exit 1
fi

echo "Python version: $(python3 --version)"
echo ""

echo "[1/3] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "[2/3] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "========================================"
echo "  ✅ Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Place your model in ./model folder"
echo "2. Run: python app.py"
echo "3. Open: http://127.0.0.1:7860"
echo ""
echo "For deployment, see: DEPLOYMENT.md"
echo ""
