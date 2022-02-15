from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import IntegrityError
from telegram import Update
from telegram.ext import CallbackContext
from app.internal.services import user_service


def start(update: Update, context: CallbackContext):
    telegram_id = update.effective_chat.id

    try:
        user = user_service.add_user(update.effective_chat.username, telegram_id)
    except IntegrityError:
        context.bot.send_message(chat_id=telegram_id, text="You are already registered")
    else:
        update.message.reply_text(f"User was registered.\nYour telegram id: {user.telegram_id}")


def set_phone(update: Update, context: CallbackContext):
    args = update.message.text.split()
    telegram_id = update.effective_chat.id

    if len(args) == 1:
        context.bot.send_message(
            chat_id=telegram_id,
            text="Set your phone number (10 digits)\nExample: /set_phone 0123456789",
        )
        return
    phone_number = args[1]

    try:
        user_service.set_phone(update.effective_chat.id, phone_number)
        message = "Phone number was updated"
    except ObjectDoesNotExist:
        message = "You're not registered \nUse /start command"
    except ValidationError:
        message = "Wrong phone number format"
    except:
        message = "Something went wrong"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def me(update: Update, context: CallbackContext):
    user = user_service.get_user_data(update.effective_chat.username)
    if not user:
        message = "You're not registered \nUse /start and /set_phone commands"
    elif not user.phone_number:
        message = "No phone number is associated with this account\nUse /set_phone command"
    else:
        message = f"Your info:\n{str(user)}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)