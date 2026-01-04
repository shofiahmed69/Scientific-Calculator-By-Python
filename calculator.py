import math
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

HISTORY_FILE = "history.txt"

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        self.current_input = ""
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg="#34495e", pady=10)
        title_frame.pack(fill="x")
        tk.Label(title_frame, text="Scientific Calculator", font=("Arial", 20, "bold"),
                bg="#34495e", fg="white").pack()
        
        # Display Frame
        display_frame = tk.Frame(self.root, bg="#2c3e50", pady=10)
        display_frame.pack(fill="x", padx=10)
        
        self.display = tk.Entry(display_frame, font=("Arial", 24), justify="right",
                               bg="#ecf0f1", fg="#2c3e50", bd=5, relief="sunken")
        self.display.pack(fill="x", ipady=15)
        
        # Result Label
        self.result_label = tk.Label(display_frame, text="", font=("Arial", 14),
                                     bg="#2c3e50", fg="#3498db", anchor="e")
        self.result_label.pack(fill="x", pady=5)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10, padx=10)
        
        # Button layout
        buttons = [
            ['sin', 'cos', 'tan', 'sqrt', 'C'],
            ['log', 'ln', 'π', 'e', '←'],
            ['7', '8', '9', '/', '^'],
            ['4', '5', '6', '*', '%'],
            ['1', '2', '3', '-', 'n!'],
            ['0', '.', '=', '+', 'abs']
        ]
        
        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#2c3e50")
            row_frame.pack()
            for btn_text in row:
                btn = tk.Button(row_frame, text=btn_text, font=("Arial", 14, "bold"),
                              width=8, height=2, command=lambda t=btn_text: self.button_click(t))
                
                # Color scheme
                if btn_text in ['C', '←']:
                    btn.config(bg="#e74c3c", fg="white", activebackground="#c0392b")
                elif btn_text == '=':
                    btn.config(bg="#27ae60", fg="white", activebackground="#229954")
                elif btn_text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'π', 'e', 'n!', 'abs']:
                    btn.config(bg="#3498db", fg="white", activebackground="#2980b9")
                elif btn_text in ['+', '-', '*', '/', '^', '%']:
                    btn.config(bg="#f39c12", fg="white", activebackground="#e67e22")
                else:
                    btn.config(bg="#95a5a6", fg="white", activebackground="#7f8c8d")
                
                btn.pack(side="left", padx=3, pady=3)
        
        # History Frame
        history_frame = tk.LabelFrame(self.root, text="History", font=("Arial", 12, "bold"),
                                     bg="#34495e", fg="white", pady=5)
        history_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.history_text = scrolledtext.ScrolledText(history_frame, height=8, width=60,
                                                     font=("Courier", 10), bg="#ecf0f1",
                                                     fg="#2c3e50", wrap=tk.WORD)
        self.history_text.pack(padx=5, pady=5, fill="both", expand=True)
        
        # History Buttons
        history_btn_frame = tk.Frame(history_frame, bg="#34495e")
        history_btn_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Button(history_btn_frame, text="Load History", command=self.load_history,
                 bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                 activebackground="#2980b9").pack(side="left", padx=5)
        tk.Button(history_btn_frame, text="Clear History", command=self.clear_history,
                 bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                 activebackground="#c0392b").pack(side="left", padx=5)
        
        self.load_history()
        
    def button_click(self, value):
        if value == 'C':
            self.display.delete(0, tk.END)
            self.result_label.config(text="")
            self.current_input = ""
        elif value == '←':
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])
        elif value == '=':
            self.calculate()
        elif value == 'π':
            self.display.insert(tk.END, str(math.pi))
        elif value == 'e':
            self.display.insert(tk.END, str(math.e))
        elif value in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'abs', 'n!']:
            self.display.insert(tk.END, value + " ")
        else:
            self.display.insert(tk.END, value)
    
    def calculate(self):
        try:
            expression = self.display.get().strip()
            if not expression:
                return
            
            # Handle scientific functions
            parts = expression.split()
            
            if len(parts) == 2 and parts[0] in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'abs', 'n!']:
                func = parts[0]
                value = float(parts[1])
                
                if func == 'sin':
                    result = math.sin(math.radians(value))
                elif func == 'cos':
                    result = math.cos(math.radians(value))
                elif func == 'tan':
                    result = math.tan(math.radians(value))
                elif func == 'sqrt':
                    if value < 0:
                        raise ValueError("Cannot calculate square root of negative number")
                    result = math.sqrt(value)
                elif func == 'log':
                    if value <= 0:
                        raise ValueError("Logarithm undefined for non-positive numbers")
                    result = math.log10(value)
                elif func == 'ln':
                    if value <= 0:
                        raise ValueError("Natural logarithm undefined for non-positive numbers")
                    result = math.log(value)
                elif func == 'abs':
                    result = abs(value)
                elif func == 'n!':
                    if value < 0 or value != int(value):
                        raise ValueError("Factorial only works for non-negative integers")
                    result = math.factorial(int(value))
            else:
                # Handle basic arithmetic
                expression = expression.replace('^', '**')
                result = eval(expression)
            
            # Format result
            if isinstance(result, float):
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 8)
            
            self.result_label.config(text=f"= {result}")
            self.save_history(expression, result)
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "Invalid expression")
    
    def save_history(self, equation, result):
        try:
            with open(HISTORY_FILE, 'a') as file:
                file.write(f"{equation} = {result}\n")
            self.load_history()
        except Exception as e:
            messagebox.showerror("Error", f"Could not save history: {e}")
    
    def load_history(self):
        try:
            self.history_text.delete(1.0, tk.END)
            with open(HISTORY_FILE, 'r') as file:
                lines = file.readlines()
                for line in reversed(lines[-20:]):  # Show last 20 entries
                    self.history_text.insert(tk.END, line)
        except FileNotFoundError:
            self.history_text.insert(tk.END, "No history yet...")
    
    def clear_history(self):
        if messagebox.askyesno("Confirm", "Clear all history?"):
            try:
                with open(HISTORY_FILE, 'w') as file:
                    pass
                self.history_text.delete(1.0, tk.END)
                self.history_text.insert(tk.END, "History cleared!")
                messagebox.showinfo("Success", "History cleared successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not clear history: {e}")

def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()