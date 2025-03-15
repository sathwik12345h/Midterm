# IS601 Mid Term Advance Calculator

## Demonstration Video
The link for the demonstartion is [here]()
## Overview
This project is a command-based calculator that supports basic arithmetic operations (addition, subtraction, multiplication, division) and includes a plugin system for extensibility. The application maintains a history of calculations and provides command-line interaction.
## Features
Basic Arithmetic Operations: Addition, subtraction, multiplication, and division.<br>
Plugin-Based Architecture: Extend functionality using plugins.<br>
History Management: Store, display, and clear past calculations.<br>
Logging: Error and usage logs.<br>
Testing Suite: Unit tests for reliability.<br>

## Setup Instructions
Follow these steps to set up and run the calculator on your local machine.

### 1. Clone the Repository
```sh
git clone git@github.com:sathwik12345h/main.git
```

### 2. Navigate to the Project Directory
```sh
cd calculator
```

### 3. Create a Virtual Environment
Set up a Python virtual environment to manage dependencies.
```sh
python -m venv venv
```

### 4. Activate the Virtual Environment
```sh
source venv/bin/activate
```

### 5. Install Dependencies
Install all required packages using:
```sh
pip install -r requirements.txt
```

### 6. Open the Project in VS Code (Optional)
If you are using VS Code, you can open the project directory with:
```sh
code .
```

## Running the Calculator
Execute the calculator program using:
```sh
python3 main.py
```

### Supported Operations
- Addition
- Subtraction
- Multiplication
- Division
- View Calculation History
- Clear Calculation History
- Delete <index>
- Exit

## Running Tests
This project includes unit tests for core arithmetic functions.

### Run Tests
```sh
pytest 
pytest --pylint
pytest --cov
```

