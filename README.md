# File Handling Tasks in Python

This project demonstrates basic file handling in Python through two simple tasks:

---

## ✅ Task 1: Read a File

This script attempts to open and read the contents of a file named `sample.txt`. If the file does not exist, it gracefully handles the error and prints a message.

### 🔹 Features
- Reads content from an existing file
- Handles `FileNotFoundError` exception

## ✅ Task 2: Write, Append, and Read from a File

This script performs the following operations on a file named `output.txt`:

1. **Write** user input to the file (overwriting any existing content)
2. **Append** additional user input to the same file
3. **Read** the final content and display it

### 🔹 Features
- Takes user input for writing and appending
- Adds each entry on a new line using `\n`
- Reads and displays final content

### 🧪 Example Run
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in python.

## 🛠 Requirements

- Python 3.x installed

---

## 🚀 How to Run

```bash
python task1.py    # For reading from sample.txt
python task2.py    # For writing, appending, and reading output.txt
Make sure to place sample.txt in the same directory if you're testing Task 1.

📁 Files
task1.py - Code for reading from a file

task2.py - Code for writing/appending/reading a file

output.txt - Created and used by Task 2

sample.txt - (Optional) Used by Task 1 if present
