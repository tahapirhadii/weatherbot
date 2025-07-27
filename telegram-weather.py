from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import requests

TOKEN = "8453202292:AAGV5X6yAID40FmZHy4SnCnbfeSzlnYgoVc"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Send me the name of the city to get the weather.")

def get_weather(city_name):
    # Placeholder for future weather API integration
    return f"Got the city {city_name}. Weather info will be here soon."

def handle_message(update: Update, context: CallbackContext):
    city = update.message.text
    weather_report = get_weather(city)
    update.message.reply_text(weather_report)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = "توکن-ربات-تو"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! بهم پیام بده تا جواب بدم.")

def echo(update: Update, context: CallbackContext):
    text_received = update.message.text
    update.message.reply_text(f"تو گفتی: {text_received}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
