import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length must be at least 1.")
            return

        # Define character sets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all character sets
        all_characters = lower + upper + digits + symbols

        # Generate the password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        password_entry.config(state=tk.NORMAL)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the password length.")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set window size and background color
root.geometry("400x250")
root.configure(bg="#2C3E50")

# Create UI elements with enhanced styles
frame = tk.Frame(root, bg="#2C3E50")
frame.pack(pady=20)

length_label = tk.Label(frame, text="Enter Password Length:", font=('Arial', 12), bg="#2C3E50", fg="white")
length_label.grid(row=0, column=0, pady=10)

length_entry = tk.Entry(frame, width=20, font=('Arial', 12), bg="#ECF0F1", relief="flat")
length_entry.grid(row=0, column=1, pady=5, padx=5)

generate_button = tk.Button(frame, text="Generate Password", command=generate_password, font=('Arial', 12), bg="#27AE60", fg="white", relief="flat", activebackground="#229954")
generate_button.grid(row=1, columnspan=2, pady=10)

password_entry = tk.Entry(frame, width=40, font=('Arial', 12), state=tk.DISABLED, bg="#ECF0F1", relief="flat")
password_entry.grid(row=2, columnspan=2, pady=5)

copy_button = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=('Arial', 12), bg="#2980B9", fg="white", relief="flat", activebackground="#2471A3")
copy_button.grid(row=3, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
