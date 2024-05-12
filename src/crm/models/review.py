from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from src.commons.models import BaseModel


class Review(BaseModel):
    product = models.ForeignKey("content.Product", on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    comment = models.TextField()
    user = models.ForeignKey("iam.User", on_delete=models.SET_NULL, related_name="reviews", null=True)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["product", "user"]
