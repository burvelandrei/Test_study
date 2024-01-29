import telebot
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def start_bot(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    red_button = telebot.types.KeyboardButton("🟥")
    black_button = telebot.types.KeyboardButton("⬛️")
    keyboard.row(red_button, black_button)
    bot.send_message(message.chat.id, "Привет! Я бот. Нажми кнопку 🟥, чтобы увидеть текущее время. Нажми кнопку ⬛️, чтобы получить прощальное сообщение.",  reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "🟥")
def handle_red_button(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, time.asctime())

@bot.message_handler(func=lambda message: message.text == "⬛️")
def handle_black_button(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Пока!")

bot.infinity_polling()