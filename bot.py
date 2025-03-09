import telebot

# Replace with your Telegram bot API token
API_KEY = "8036073435:AAGx2nJAub8C

JkEBBjEPkGkT-jocyzeePYI"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(func=lambda message: True)
def respond(message):
    response = f"You said: {message.text}"  # Simple echo bot (Replace with AI response logic)
    bot.send_message(message.chat.id, response)

bot.polling()
