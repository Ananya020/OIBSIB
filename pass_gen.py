import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        if password:
            password_var.set(password)

    root = tk.Tk()
    root.title("Password Generator")

    main_frame = ttk.Frame(root, padding="20", style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    style = ttk.Style()
    style.configure("Main.TFrame", background="#F0F0F0")

    length_label = ttk.Label(main_frame, text="Password Length:", style="Label.TLabel")
    length_label.grid(row=0, column=0, sticky=tk.W)

    length_entry = ttk.Entry(main_frame)
    length_entry.grid(row=0, column=1, sticky=tk.W)

    letters_var = tk.BooleanVar()
    letters_check = ttk.Checkbutton(main_frame, text="Include Letters", variable=letters_var, style="Checkbutton.TCheckbutton")
    letters_check.grid(row=1, column=0, sticky=tk.W)

    numbers_var = tk.BooleanVar()
    numbers_check = ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var, style="Checkbutton.TCheckbutton")
    numbers_check.grid(row=2, column=0, sticky=tk.W)

    symbols_var = tk.BooleanVar()
    symbols_check = ttk.Checkbutton(main_frame, text="Include Symbols", variable=symbols_var, style="Checkbutton.TCheckbutton")
    symbols_check.grid(row=3, column=0, sticky=tk.W)

    generate_button = ttk.Button(main_frame, text="Generate Password", command=generate, style="Generate.TButton")
    generate_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

    password_var = tk.StringVar()
    password_label = ttk.Label(main_frame, text="Generated Password:", style="Label.TLabel")
    password_label.grid(row=5, column=0, sticky=tk.W, pady=(10, 0))

    password_entry = ttk.Entry(main_frame, textvariable=password_var, state='readonly')
    password_entry.grid(row=5, column=1, sticky=tk.W, pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    generate_password_gui()

