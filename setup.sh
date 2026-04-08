#!/bin/bash

echo "🚀 Setting up ETL project structure..."

# Create folders
mkdir -p data/raw data/processed
mkdir -p src notebooks tests

# Create Python files
touch src/extract.py
touch src/transform.py
touch src/load.py
touch src/main.py

# Create root files
touch requirements.txt README.md .gitignore

echo "✅ Project structure created successfully!"
