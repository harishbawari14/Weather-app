# text to speech 
# import the required module from text to speech conversion 
import win32com.client 
  
# Calling the Dispatch method of the module which  
# interact with Microsoft Speech SDK to speak 
# the given input from the keyboard 
  
speaker = win32com.client.Dispatch("SAPI.SpVoice")

import requests
import json

while True:
  
  city = input("Enter the name of the city\n")

  if city == 'q':
    speaker.Speak("Goodbye")
    break
  
  url = f"http://api.weatherapi.com/v1/current.json?key=50cf42cb12704c888d963839252702&q={city}"

  r = requests.get(url)
# print(r.text)
# print(type(r.text))
  dic =json.loads(r.text)

#   temp:
  celsius = (dic['current']['temp_c'])
#   print(dic['current']['temp_c'])
#   fahrenheit = (dic['current']['temp_f'])
  humidity = (dic['current']['humidity'])
  last_update = (dic['current']['last_updated'])
  print(celsius)
#   print(fahrenheit)
  print(humidity)
  print(last_update)
#   print(type(dic))

  speaker.Speak(f"The current temperature in {city} is {celsius} degrees") 
#   speaker.Speak(f"The current weather in {city} is {fahrenheit} degrees") 
  speaker.Speak(f"The current humidity in {city} is {humidity} degrees") 
  speaker.Speak(f"The last update of {city} is {last_update} day") 