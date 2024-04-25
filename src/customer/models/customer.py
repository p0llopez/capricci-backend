from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.db import models

from src.commons.models import BaseModel


class Customer(BaseModel):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_name = models.CharField(max_length=255)
    password = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})",
                message="Password must have more than 8 characters, symbols, numbers, uppercase and lowercase",
            )
        ],
    )
    phone_number = models.CharField(max_length=255)
    points = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_email"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.phone_number = self.phone_number.replace(" ", "").replace("-", "").replace("+", "")
        self.password = make_password(self.password)
        return super().save(*args, **kwargs)
