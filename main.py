import openai
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Set up OpenAI API key
openai.api_key = "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"

# Set up Telegram bot token
telegram_bot_token = "5728411264:AAHhfWnZwudIK7cWFKYpJwicDh0JLOAP55Q"

# Set up Telegram bot updater
updater = Updater(token=telegram_bot_token, use_context=True)

# Define message handler
def handle_message(update, context):
    # Get user input message
    user_message = update.message.text

    # Call OpenAI API to get response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        top_p=1,
        #temperature=0.9,
        max_tokens=512
    )

    # Get response from OpenAI API
    bot_message = response.choices[0].text.strip()

    # Send response back to user
    context.bot.send_message(chat_id=update.effective_chat.id, text=bot_message)

# Set up message handler for Telegram bot
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
updater.dispatcher.add_handler(message_handler)

# Start Telegram bot
updater.start_polling()
