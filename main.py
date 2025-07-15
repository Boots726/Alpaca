# Entry point: starts AI and Telegram bot
from trader import TraderBot
from telegram_bot import start_bot

if __name__ == '__main__':
    bot = TraderBot()
    start_bot(bot)