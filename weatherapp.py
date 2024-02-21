import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

def get_weather(api_key, location):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location_name = data['location']['name']
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        condition = data['current']['condition']['text']
        return location_name, temperature, humidity, condition
    else:
        return None

def display_weather(location, temperature, humidity, condition):
    result_window = tk.Toplevel()
    result_window.title("Weather Report")

    location_label = ttk.Label(result_window, text=f"Weather in {location}:", font=("Helvetica", 14, "bold"))
    location_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    temp_label = ttk.Label(result_window, text=f"Temperature: {temperature}°C", font=("Helvetica", 12))
    temp_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    humidity_label = ttk.Label(result_window, text=f"Humidity: {humidity}%", font=("Helvetica", 12))
    humidity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    condition_label = ttk.Label(result_window, text=f"Condition: {condition}", font=("Helvetica", 12))
    condition_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

def fetch_and_display_weather(api_key, location):
    weather_data = get_weather(api_key, location)
    if weather_data:
        display_weather(*weather_data)
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data.")

def main():
    root = tk.Tk()
    root.title("Weather App")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    location_label = ttk.Label(main_frame, text="Enter location:")
    location_label.grid(row=0, column=0, sticky="w")

    location_entry = ttk.Entry(main_frame)
    location_entry.grid(row=0, column=1, padx=5, pady=5)

    api_key = "072cbe4f90864907b2a161408240902"

    def on_submit():
        location = location_entry.get()
        fetch_and_display_weather(api_key, location)

    submit_button = ttk.Button(main_frame, text="Get Weather", command=on_submit)
    submit_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()

if __name__ == "__main__":
    main()
