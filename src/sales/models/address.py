from django.db import models

from src.commons.models import BaseModel


class Address(BaseModel):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    user = models.ForeignKey("iam.User", on_delete=models.CASCADE)
    order = models.ForeignKey("sales.Order", on_delete=models.CASCADE, related_name="addresses")

    class Meta:
        unique_together = ("user", "order")

    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}, {self.zip_code}"
