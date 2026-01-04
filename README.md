# 🧮 Scientific Calculator

A modern, feature-rich scientific calculator built with Python and Tkinter. Perform basic arithmetic operations alongside advanced scientific calculations with an intuitive graphical user interface.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## ✨ Features

### Basic Operations
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔢 Modulo (%)
- ⚡ Power (^)

### Scientific Functions
- 📐 **Trigonometry**: sin, cos, tan (in degrees)
- √ **Square Root**
- 📊 **Logarithms**: log (base 10), ln (natural log)
- 🔢 **Factorial** (n!)
- 📏 **Absolute Value**
- 🥧 **Constants**: π (pi) and e

### Additional Features
- 📜 **History Panel**: View your last 20 calculations
- 💾 **Persistent Storage**: All calculations are saved to `history.txt`
- 🎨 **Modern UI**: Clean, color-coded interface
- ⌫ **Backspace**: Fix mistakes easily
- 🗑️ **Clear Functions**: Clear current input or entire history

## 🖼️ Screenshots

<img width="882" height="995" alt="image" src="https://github.com/user-attachments/assets/cdf89417-c5cc-4b94-805b-d7e28823b9d5" />


## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/scientific-calculator.git
cd scientific-calculator
```

2. Run the calculator:
```bash
python calculator.py
```

That's it! No additional dependencies required.

## 📖 Usage

### Basic Calculations
1. Click number buttons to enter values
2. Click an operator (+, -, *, /, ^, %)
3. Enter the second number
4. Press `=` to calculate

**Example**: `5 + 3 =` → Result: 8

### Scientific Functions
1. Click the function button (sin, cos, sqrt, etc.)
2. Enter the value
3. Press `=` to calculate

**Example**: `sqrt 16 =` → Result: 4

### Using Constants
- Click `π` to insert 3.14159...
- Click `e` to insert 2.71828...

**Example**: `π * 2 =` → Result: 6.28318531

### Managing History
- Click **"Load History"** to refresh the history panel
- Click **"Clear History"** to delete all saved calculations
- History is automatically saved to `history.txt`

## 🎨 Color Coding

- 🔴 **Red Buttons**: Clear (C) and Backspace (←)
- 🟢 **Green Button**: Equals (=)
- 🔵 **Blue Buttons**: Scientific functions
- 🟠 **Orange Buttons**: Arithmetic operators
- ⚪ **Gray Buttons**: Numbers and decimal point

## 📁 Project Structure

```
scientific-calculator/
│
├── calculator.py       # Main application file
├── history.txt        # Calculation history (auto-generated)
├── README.md          # This file
└── LICENSE            # License file
```

## 🛠️ Technical Details

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Math Library**: Python's built-in `math` module
- **File I/O**: Text file for persistent history storage

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Ideas for Contribution
- Add more scientific functions (sinh, cosh, tanh, etc.)
- Implement calculation history search
- Add keyboard shortcuts
- Support for complex numbers
- Memory functions (M+, M-, MR, MC)
- Export history to CSV/PDF
- Dark/Light theme toggle

## 🐛 Known Issues

- Very large factorial calculations may take time to compute
- Trigonometric functions work in degrees (not radians)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Built with Python and Tkinter
- Inspired by modern calculator designs
- Thanks to the Python community for excellent documentation

## 📞 Support

If you have any questions or run into issues:
- Contact me via email - frex19shofi@gmail.com

---

⭐ If you found this project helpful, please consider giving it a star!

**Made with ❤️ and Python**
