from cgitb import text
from gettext import find
from importlib import resources
from wsgiref.util import request_uri
import telebot 
import requests
cities=[{"ru":"Абакан",	"en":"Abakan"},
{"ru":"Альметьевск",	"en":"Almetyevsk"},
{"ru":"Анадырь",	"en":"Anadyr"},
{"ru":"Анапа",	"en":"Anapa"},
{"ru":"Архангельск",	"en":"Arkhangelsk"},
{"ru":"Астрахань",	"en":"Astrakhan"},
{"ru":"Москва",	"en":"Moscow"},
{"ru":"Сочи",	"en":"Sochi"} ] 

def find_city(city_ru):
  for city in cities:
    if city['ru'].find(city_ru)!=-1:
      return city["en"]
  return False
print(find_city("Сочи"))
apiToken='3f35132f857ce32ea44d0392cfe17fc6'
host='https://api.openweathermap.org/data/2.5/find'
host2='https://api.openweathermap.org/data/2.5/weather'
def get_weather(city):
  try:
    res=requests.get(host, params={'q': city +',RU', 'type':'like', 'units':'metric', 'APPID':apiToken})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
  except Exception as e:
    print("Exception (find):", e)
    pass

  try: 
    resources= requests.get(host2, params={'id': city_id, 'lang':'roll', 'units':'metric', 'APPID':apiToken})
    data=resources.json()
    return data 
  except Exception as e:
    print("Exception (weather):", e)
    pass


# print(get_weather("Moscow")["main"]["temp"])
token="5313147862:AAGzI8czc9v3S65mFs0tAsNAxqdS2oGBJhc"
bot=telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message, res=False):
  bot.send_message(message.chat.id, 'Добрый день!')

@bot.message_handler(content_types="text")
def message_text(message):
  print(message.text, message.text == 'как погода в Москве?')
  if message.text == "привет":
    bot.send_message(message.chat.id, "привет!")
  elif message.text == "пока":
    bot.send_message(message.chat.id, "досвидания, хорошего дня.")
  # elif message.text == 'как погода в Москве?':
  #   bot.send_message(message.chat.id, 'сейчас погода в Москве --  '+str(get_weather("Moscow")["main"]["temp"]))
  # elif message.text == 'как погода в Сочи':
  #   bot.send_message(message.chat.id, 'сейчас погода в Сочи --  '+str(get_weather("Sochi")["main"]["temp"]))

  elif message.text.find('погода')!=-1:
    city_name=message.text.split(" ")[-1][0:-2]
    city_name_en=find_city(city_name)
    if find_city(city_name):
      bot.send_message(message.chat.id, 'сейчас погода в '+ message.text.split(" ")[-1][0:-1] + ' --  '+str(get_weather(city_name_en)["main"]["temp"]))
      bot.send_message(message.chat.id, 'сейчас погода в '+ message.text.split(" ")[-1][0:-1] + ' --  '+str(get_weather(city_name_en)["main"]))
    
    else:
      bot.send_message(message.chat.id, "город не найден.")
bot.infinity_polling()





"""
1 вместо москвы искать любой город, который передается в функцию 
2 вызывать функцию при обработке сообщения
"""