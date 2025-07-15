
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def start_bot(trader):
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    def status(update: Update, context: CallbackContext):
        update.message.reply_text("Bot is running.")

    def stop(update: Update, context: CallbackContext):
        trader.stop()
        update.message.reply_text("Trading stopped.")

    dispatcher.add_handler(CommandHandler("status", status))
    dispatcher.add_handler(CommandHandler("stop", stop))

    updater.start_polling()
    updater.idle()
