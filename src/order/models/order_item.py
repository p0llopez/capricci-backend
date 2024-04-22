from django.db import models

from src.commons.models import BaseModel


class OrderItem(BaseModel):
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
