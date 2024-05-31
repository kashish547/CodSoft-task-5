import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
    except ValueError as e:
        password_var.set("Invalid length")
        return
    
    include_upper = upper_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    password_var.set(password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="#2e2e2e")

# Password length
length_label = tk.Label(root, text="Length of password:", font=("Arial", 14), bg="#2e2e2e", fg="#ffffff")
length_label.pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 14), bg="#f0f0f0", fg="#000000")
length_entry.pack(pady=10)

# Options for including upper case letters, numbers, and symbols
upper_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff", selectcolor="#2e2e2e")
upper_check.pack(pady=5)

numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff", selectcolor="#2e2e2e")
numbers_check.pack(pady=5)

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff", selectcolor="#2e2e2e")
symbols_check.pack(pady=5)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 14, "bold"), bg="#4caf50", fg="#ffffff")
generate_button.pack(pady=20)

# Entry to display the generated password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), bg="#f0f0f0", fg="#000000", state='readonly')
password_entry.pack(pady=10)

# Run the main application loop
root.mainloop()
