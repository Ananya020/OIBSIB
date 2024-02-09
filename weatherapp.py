import requests

def get_weather( api_key, location ):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"

    response= requests.get(url)
    if response.status_code== 200:
        data = response.json()
        location_name = data['location']['name']
        temperature = data['current']['temp_c']
        humidity = data['current']['humidity']
        condition = data['current']['condition']['text']
        
        print(f"Weather in {location_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")
    
    else:
        print("Failed to retrieve weather data.")

def main():
    api_key = " 072cbe4f90864907b2a161408240902"
    location = input("Enter the location:  ")
    get_weather(api_key, location)
        
if __name__ == "__main__":
    main()        
    
