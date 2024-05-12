from django.db import models

from src.commons.models import BaseModel


class Order(BaseModel):
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    items_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    user = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    address = models.ForeignKey("sales.Address", on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name} {self.user.last_name}"
