# Regular Grammar Parser

A Python-based tool to parse regular grammars, convert them into Non-deterministic Finite Automata (NFA), validate strings against the NFA, and visualize the NFA as a graph.

---

## 🚀 Features

- **Grammar Parsing**: Parse regular grammar rules in a user-friendly format.
- **NFA Conversion**: Automatically convert grammar rules into an NFA.
- **String Validation**: Check if a string is accepted by the grammar.
- **NFA Visualization**: Generate a graphical representation of the NFA using Graphviz.

---

## 🛠 Requirements

- Python 3.7 or higher
- `graphviz` library (for NFA visualization)

---

## 📦 Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Hassaankh10/Regular_Grammar_Parser
   cd Regular_Grammar_Parser
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Graphviz**:
   - On macOS:
     ```bash
     brew install graphviz
     ```
   - On Linux:
     ```bash
     sudo apt-get install graphviz
     ```
   - On Windows:
     Download and install Graphviz from [Graphviz.org](https://graphviz.org/).

5. **Run the Application**:
   ```bash
   python main.py
   ```

---

## 📝 Usage

1. **Start the Program**:
   Run the following command:
   ```bash
   python main.py
   ```

2. **Enter Grammar Rules**:
   - Input grammar rules in the format:
     ```
     S -> aA | bB
     A -> a
     B -> b
     ```
   - Type `done` when you are finished entering rules.

3. **Validate Strings**:
   - Enter strings to validate against the grammar.
   - Type `exit` to quit the program.

4. **View the NFA**:
   - The NFA will be saved as a PNG file (`nfa.png`) in the project directory.

---

## 📖 Example

### Input:
```
Enter grammar rules (e.g., S -> aA | bB). Type 'done' to finish:
S -> aA | bB
A -> a
B -> b
done
Enter string to validate (or 'exit' to quit): aa
Enter string to validate (or 'exit' to quit): ab
Enter string to validate (or 'exit' to quit): exit
```

### Output:
- **NFA Visualization**: A PNG file named `nfa.png` will be generated.
- **String Validation Results**:
  ```
  Accepted
  Rejected
  ```

---

## 📂 Project Structure

- **`main.py`**: The entry point of the application.
- **`custom_parser.py`**: Functions to parse grammar and convert it to NFA.
- **`validator.py`**: Validates strings against the NFA.
- **`visualizer.py`**: Visualizes the NFA using Graphviz.
- **`requirements.txt`**: Lists the required Python dependencies.
- **`LICENSE`**: MIT License for the project.

---

## 🛡 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

---

## 👤 Author

- **Hassaankh10** - [GitHub Profile](https://github.com/Hassaankh10)