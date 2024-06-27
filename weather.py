import requests
api_key = 'c138b036346e8f435f8dbe96ede852cd'
user_inp = input("Enter City:")
weather_data= requests.get(
     f"https://api.openweathermap.org/data/2.5/weather?q={user_inp}&units=imperial&APPID={api_key}")

if(weather_data.json()['cod']=='404'):
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])

    print(f"The Weather in {user_inp} is:{weather}")
    print(f"The temprature in {user_inp} is {temp} ºF")