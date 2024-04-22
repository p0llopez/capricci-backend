from django.db import models

from src.commons.models import BaseModel


class Address(BaseModel):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
