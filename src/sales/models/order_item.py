from django.db import models

from src.commons.models import BaseModel


class OrderItem(BaseModel):
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    product = models.ForeignKey("content.Product", on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.order.id} - {self.product.name} x {self.quantity}"