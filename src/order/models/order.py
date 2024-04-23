from django.db import models

from src.commons.models import BaseModel


class Order(BaseModel):
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    items_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    shipping_address = models.ForeignKey("customer.Address", on_delete=models.CASCADE)