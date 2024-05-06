#fetching api
import requests
api_key = 'b43024dac1f8970cb16d342c3351e66f'
user_input = input("Enter city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#converting the temp from farenheits to celcius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

#basic error handling
if weather_data.json()['cod'] == '404':
    print("oops :( your city doesnt exist")
else:
    #fetching deatails about the conditions 
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    temp_celsius = fahrenheit_to_celsius(temp)
    humidity = weather_data.json()['main']['humidity']
    pressure = weather_data.json()['main']['pressure']
    visibility = weather_data.json()['visibility']
    wind_speed = weather_data.json()['wind']['speed']

    #printing the details
    print("The weather in {} is: {}".format(user_input, weather))
    print("The temperature in {} is: {}°F or {}°C".format(user_input, temp, round(temp_celsius,1)))
    print("The humidity in {} is: {}%".format(user_input, humidity))
    print("The pressure in {} is: {} hPa".format(user_input, pressure))
    print("The visibility in {} is: {} meters".format(user_input, visibility))
    print("The wind speed in {} is: {} m/s".format(user_input, wind_speed))
    




