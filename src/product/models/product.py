from django.db import models

from src.commons.models import BaseModel


class Product(BaseModel):
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    presentation = models.PositiveIntegerField
    presentation_format = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
