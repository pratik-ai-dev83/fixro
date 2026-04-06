# Fixro – AI Bug Fixer

Fixro is a simple AI-powered tool that analyzes your code and suggests possible bug fixes.
It helps developers quickly identify errors and improve code quality in seconds.

---

## Features

* Analyze code for errors and issues
* Suggest possible fixes
* Beginner-friendly interface
* Fast and lightweight
* CLI-based (runs in terminal)

---

## Tech Stack

* Python 🐍
* AST (Abstract Syntax Tree) for code parsing
* Optional: OpenAI API (for future AI improvements)

---

## Project Structure

```
Fixro/
│── main.py          # Main program
│── analyzer.py      # Code analysis logic
│── fixer.py         # Suggest fixes
│── utils.py         # Helper functions
│── README.md        # Documentation
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pratik-ai-dev83/fixro.git
```

2. Go to project folder:

```bash
cd fixro
```

3. (Optional) Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python main.py
```

### Steps:

1. Paste your code
2. Type `END`
3. View detected issues
4. Get suggested fixes

---

## How It Works

* User inputs code through terminal
* `analyzer.py` scans for syntax errors and bad practices
* `fixer.py` generates suggestions
* Results are displayed instantly

---

## Example

### Input:

```python
x = 10
print(x)
```

### Output:

```
 Issues Found:
1. Line 2: Debug print statement found

 Suggested Fixes:
- Remove or replace debug print statements with logging
```

---

## Future Improvements

* Web-based interface
* AI-powered auto code fixing
* Code quality scoring system
* File upload support
* User authentication

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`feature-new`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## License

This project is open-source and available under the MIT License.

---

## Support

If you like this project, please give it a ⭐ on GitHub!

---

## Author

Developed by Pratik Patil
Thank You!!
---
