import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

response = ""
# Установка API-ключа OpenAI GPT
openai.api_key = "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"

# Функция для генерации ответа с помощью OpenAI
def generate_response_from_prompt(prompt):
    # TODO: вызвать OpenAI GPT и сгенерировать ответ
    return response

# Функция обработки сообщений от пользователей в Telegram
def handle_message(bot, update):
    user_input = update.message.text
    response = generate_response_from_prompt(user_input)

    # Отправка сгенерированного ответа пользователю в Telegram
    bot.send_message(chat_id=update.message.chat_id, text=response)

# Создание бота и добавление обработчиков сообщений
bot = telegram.Bot(token="5728411264:AAHhfWnZwudIK7cWFKYpJwicDh0JLOAP55Q")
updater = Updater(token="5728411264:AAHhfWnZwudIK7cWFKYpJwicDh0JLOAP55Q")
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

# Запуск бота
updater.start_polling()

