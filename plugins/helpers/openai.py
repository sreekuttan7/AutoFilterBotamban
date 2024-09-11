import telebot
from telebot import types

# Replace with your actual bt token
BOT_TOKEN = "6815093612:AAEA_7V2a-G_yQ3Zw2IpxV_iWQqm64liTcI"

# Create the bot instance
bot = telebot.TeleBot(BOT_TOKEN)

# Store the state of autofilter for each chat
autofilter_state = {}

# Define the keyboard for autofilter options
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard.add(types.KeyboardButton("Autofilter On"), types.KeyboardButton("Autofilter Off"))

# Handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
  chat_id = message.chat.id
  # Initialize autofilter state for the chat
  autofilter_state[chat_id] = False
  bot.send_message(chat_id, "Welcome! Use /autofilter to toggle autofilter.")

# Handle the /autofilter command
@bot.message_handler(commands=['autofilter'])
def autofilter_command(message):
  chat_id = message.chat.id
  # Toggle the autofilter state
  autofilter_state[chat_id] = not autofilter_state[chat_id]
  if autofilter_state[chat_id]:
    bot.send_message(chat_id, "Autofilter is now **ON**.", reply_markup=keyboard)
  else:
    bot.send_message(chat_id, "Autofilter is now **OFF**.", reply_markup=keyboard)

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
  chat_id = message.chat.id
  if autofilter_state[chat_id]:
    # Your autofilter logic here
    # Example:
    filtered_message = message.text.replace("badword", "***")
    bot.send_message(chat_id, filtered_message)
  else:
    bot.send_message(chat_id, message.text)

# Start the bot
bot.polling()
