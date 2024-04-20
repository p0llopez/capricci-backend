from django.contrib.auth.models import AbstractUser

from src.commons.models import BaseModel


class User(BaseModel, AbstractUser):
    # ...
    pass
