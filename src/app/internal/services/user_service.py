import re
from django.core.exceptions import ValidationError
from app.internal.models.user import User


def add_user(telegram_username, telegram_id):
    return User.objects.create(telegram_username=telegram_username, telegram_id=telegram_id)


def set_phone(telegram_id, phone_number):
    if not re.match(r'^\d{10}$', phone_number):
        raise ValidationError('Incorrect phone number')
    user = User.objects.get(telegram_id=telegram_id)
    user.phone_number = phone_number
    user.save()


def get_user_data(telegram_username):
    return User.objects.get(telegram_username=telegram_username)