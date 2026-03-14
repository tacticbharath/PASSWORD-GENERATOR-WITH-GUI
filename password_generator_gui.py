import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())

        characters = ""

        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        password = "".join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number for length")

# Function to copy password
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Secure Password Generator",bg='pink', font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Password Length
length_frame = tk.Frame(root)
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Password Length:")
length_label.pack(side=tk.LEFT)

length_entry = tk.Entry(length_frame, width=5)
length_entry.pack(side=tk.LEFT, padx=5)
length_entry.insert(0, "12")

# Options
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root)
options_frame.pack(pady=10)

letters_check = tk.Checkbutton(options_frame, text="Letters", variable=letters_var)
letters_check.grid(row=0, column=0, padx=10)

numbers_check = tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var)
numbers_check.grid(row=0, column=1, padx=10)

symbols_check = tk.Checkbutton(options_frame, text="Symbols", variable=symbols_var)
symbols_check.grid(row=0, column=2, padx=10)

# Generate Button
generate_btn = tk.Button(root, text="Generate Random Password", command=generate_password, bg="#4CAF50", fg="white")
generate_btn.pack(pady=10)

# Password Output
password_entry = tk.Entry(root, width=30, font=("Arial", 12))
password_entry.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_btn.pack(pady=5)

# Run GUI
root.mainloop()
