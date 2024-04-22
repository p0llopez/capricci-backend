from django.db import models

from src.commons.models import BaseModel


class Customer(BaseModel):
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    points = models.IntegerField()
    username = models.CharField(max_length=255)
