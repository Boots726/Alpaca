
from telegram_bot import start_bot
from trader import TraderBot

if __name__ == "__main__":
    bot = TraderBot()
    bot.run()
    start_bot(bot)
