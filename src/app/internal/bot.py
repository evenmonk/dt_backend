import inspect
from telegram.ext import Updater, CommandHandler
from config.settings import TELEGRAM_BOT_TOKEN
from app.internal.transport.bot import handlers

# def add_handlers(update: Updater):
#     updater.dispatcher.add_handler(start())

# def run():
#     updater = Updater(TELEGRAM_BOT_TOKEN)
#     add_handlers(updater)
    
#     updater.start_polling()
#     updater.idle()

# run()
def run():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    add_handlers(updater)
    updater.start_polling()
    updater.idle()

def add_handlers(updater: Updater):
    handlers_functions = inspect.getmembers(handlers, inspect.isfunction)
    dispatcher = updater.dispatcher
    for handler_function in handlers_functions:
        current_handler = CommandHandler(handler_function[0], handler_function[1])
        dispatcher.add_handler(current_handler)

if __name__ == '__main__':
    run()