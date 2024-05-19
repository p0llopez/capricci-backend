from django.contrib.auth.models import AbstractUser
from django.db import models

from src.commons.models import BaseModel


class User(BaseModel, AbstractUser):
    points = models.IntegerField(default=0)
