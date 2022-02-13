from django.core.validators import RegexValidator
from django.db import models


class User(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="phone number should contain 10 digits without country code"
    )
    telegram_username = models.CharField(db_index=True, max_length=255, unique=True)
    telegram_id = models.CharField(db_index=True, max_length=255, unique=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    