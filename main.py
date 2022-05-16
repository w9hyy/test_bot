import telebot
token="5313147862:AAGzI8czc9v3S65mFs0tAsNAxqdS2oGBJhc"
bot=telebot.TeleBot(token)


@bot.message_handler(content_types="text")
def message_text(message):
  if message.text == "privet":
    bot.send_message(message.chat.id, "good morning!")
  elif message.text == "poka":
    bot.send_message(message.chat.id, "good bye!")
  else:

    bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
