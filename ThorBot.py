import contants as keys
import ThorBotRes as R
from telegram.ext import *

print("U2mp3Bot started...")


def start_command(update, context):
    update.message.reply_text('Enter magnet link!')

def help_command(update,context):
    update.message.reply_text('testing')

def handle_message(update, context):
    text = str(update.message.text)
    response = R.bot_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()