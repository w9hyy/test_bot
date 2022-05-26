import telebot 
import requests


apiToken='3f35132f857ce32ea44d0392cfe17fc6'
host='https://api.openweathermap.org/data/2.5/find'

def get_weather():
  sity = "Moscow"
  try:
    res=requests.get(host, params={'q': sity +',RU', 'type':'like', 'units':'metric', 'APPID':apiToken})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
  except Exception as e:
    print("Exception (find):", e)
    pass

    sity = "new york"
  try:
    res=requests.get(host, params={'q': sity +',RU', 'type':'like', 'units':'metric', 'APPID':apiToken})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]
    print("city:", cities)
    city_id = data['list'][0]['id']
    print('city_id=', city_id)
  except Exception as e:
    print("Exception (find):", e)
    pass

get_weather()
token="5313147862:AAGzI8czc9v3S65mFs0tAsNAxqdS2oGBJhc"
bot=telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def start(message, res=False):
  bot.send_message(message.chat.id, 'привет')

@bot.message_handler(content_types="text")
def message_text(message):
  print(message.text, message.text == 'как погода?')
  if message.text == "privet":
    bot.send_message(message.chat.id, "good morning!")
  elif message.text == "poka":
    bot.send_message(message.chat.id, "good bye!")
  elif message.text == 'как погода?':
    bot.send_message(message.chat.id, 'хорошая')

  get_weather("mess")
  # else:
  #   bot.send_message(message.chat.id, message.text)


bot.infinity_polling()

"""
1 вместо москвы искать любой город, который передается в функцию 
2 вызывать функцию при обработке сообщения
"""