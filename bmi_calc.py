import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to save BMI data to database
def save_bmi_to_db(weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS bmi_records (weight REAL, height REAL, bmi REAL, category TEXT)")
    c.execute("INSERT INTO bmi_records VALUES (?, ?, ?, ?)", (weight, height, bmi, category))
    conn.commit()
    conn.close()

# Function to plot BMI trend
def plot_bmi_trend():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT bmi FROM bmi_records")
    data = c.fetchall()
    bmi_values = [record[0] for record in data]
    conn.close()

    plt.plot(bmi_values)
    plt.xlabel('Record Number')
    plt.ylabel('BMI')
    plt.title('BMI Trend')
    plt.show()

# Function to handle calculate button click
def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is: {bmi:.2f}\nCategory: {category}")

        save_bmi_to_db(weight, height, bmi, category)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to handle plot button click
def on_plot():
    plot_bmi_trend()

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Create input fields
weight_label = tk.Label(root, text="Enter your weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Enter your height (m):")
height_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=on_calculate)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=10, pady=5)

# Create plot button
plot_button = tk.Button(root, text="Plot BMI Trend", command=on_plot)
plot_button.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()
