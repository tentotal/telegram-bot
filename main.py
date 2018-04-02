import telebot
import sqlite3
import random

token = "451307364:AAETEiun562uOpN5R6RJy8p-nuspeLhXjy0"
bot = telebot.TeleBot(token)

def get_data(mood):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM BlueCheese WHERE mood = (?)", (mood,))
    data = c.fetchall()
    c.close()
    conn.close()
    n = random.randrange(0, len(data))
    return data[n]

@bot.message_handler(commands=['start'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = 1)
    user_markup.row("Chill", "Fresh Tunes")
    user_markup.row("All The Way Up", "Essentials")
    bot.send_message(message.chat.id, "What can I get you?", reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = 1)
    user_markup.row("Chill", "Fresh Tunes")
    user_markup.row("All The Way Up", "Essentials")
    bot.send_message(message.chat.id, "Сhoose whatever you like!", reply_markup=user_markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    mood = ["Chill", "Fresh Tunes", "All The Way Up", "Essentials"]
    if message.text in mood:
        data = get_data(message.text)
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Apple Music", url=data[1])
        keyboard.add(url_button)
        bot.send_photo(message.chat.id, data[2], caption = data[3], reply_markup=keyboard)

bot.polling(none_stop = True, interval = 0)
