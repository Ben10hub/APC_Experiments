import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple GUI Application")
root.geometry("350x250")

# Heading
heading = tk.Label(root, text="Welcome to Python GUI")
heading.pack(pady=15)

# Input field
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Button function
def greet():
    name = name_entry.get()

    if name:
        messagebox.showinfo("Greeting", "Hello, " + name + "!")
    else:
        messagebox.showwarning("Warning", "Please enter your name")

# Button
button = tk.Button(root, text="Submit", command=greet)
button.pack(pady=15)

# Run application
root.mainloop()