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
    
    def __str__(self):
        return (
            f"username: {self.telegram_username}\n"
            f"telegram_id: {self.telegram_id}\n"
            f"phone number: {self.phone_number}"
        )