import requests
import json

# Установите API-ключ и модель OpenAI GPT-3
API_KEY = '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'
MODEL_ID = 'GPT-3'

# Функция для генерации ответа с помощью OpenAI GPT-3
def generate_response_from_prompt(prompt):
    # Создайте запрос к API OpenAI GPT-3
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    data = {
        'prompt': prompt,
        'max_tokens': 128,
        'temperature': 0.7,
        'n': 1,
        'stop': '\n'
    }

    response = requests.post(f'https://api.openai.com/v1/models/{MODEL_ID}/completions', headers=headers, data=json.dumps(data))

    # Обработка ответа
    if response.status_code == 200:
        text = response.json()['choices'][0]['text']
        return text
    else:
        print(f'Ошибка при обработке запроса: {response.status_code}')
        return "К сожалению, я не могу ответить на ваш вопрос в данное время."

# Функция обработки сообщений от пользователей в Telegram
def handle_message(update, context):
    user_input = update.message.text
    response = generate_response_from_prompt(user_input)

    # Отправка сгенерированного ответа пользователю в Telegram
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

# Добавление обработчиков сообщений
updater = Updater(token='5728411264:AAHhfWnZwudIK7cWFKYpJwicDh0JLOAP55Q', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Запуск бота
updater.start_polling()
updater.idle()