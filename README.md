# 🧪 Calculator Test Suite using Pytest

This project tests a simple **Calculator** app using **Pytest**.  
It includes class-based test cases and uses fixtures to reuse the Calculator instance for all tests.

## ✅ Features
- Test basic operations: `add`, `subtract`, `multiply`, `divide`
- Class-based test structure using `TestCalculator`
- Reusable setup using `@pytest.fixture`
- Handles divide by zero with proper exception handling

## 📁 Project Structure

```text
calculator_project/
├── calculator.py         # Calculator logic
├── conftest.py           # Pytest fixture
└── test_calculator.py    # Test cases using a test class
```

## ▶️ How to Run Tests
Make sure you have `pytest` installed, then run:
```bash
pytest
```

## 🖼️ Test Result Screenshot

![Test Result](Screenshot%20(733).png)





