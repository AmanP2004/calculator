import tkinter as tk
from tkinter import messagebox

def press_key(key):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + key)

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_button(root, text, row, col, func=None):
    return tk.Button(root, text=text, padx=20, pady=10, command=lambda: func(text) if func else press_key(text)).grid(row=row, column=col)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create display entry
entry_display = tk.Entry(root, width=30, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons for calculator
for i, label in enumerate(button_labels):
    if label == '=':
        create_button(root, label, i // 4 + 1, i % 4, calculate)
    else:
        create_button(root, label, i // 4 + 1, i % 4)

# Create Clear button
create_button(root, 'C', 5, 0, clear_display)

# Run the application
root.mainloop()
