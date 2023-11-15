import tkinter as tk

# Function to perform mathematical operations
def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Functional Calculator")

# Create the entry field
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col)

# Add a clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=3)

# Add an equal button
equal_button = tk.Button(root, text="=", padx=20, pady=20, command=calculate)
equal_button.grid(row=5, column=3)

# Run the application
root.mainloop()