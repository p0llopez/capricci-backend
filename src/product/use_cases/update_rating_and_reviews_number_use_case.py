from uuid import UUID

from django.db import transaction
from django.db.models import Sum

from src.product.models import Product


class UpdateRatingAndReviewsNumberUseCase:
    def __call__(self, product_id: UUID):
        product = Product.objects.get(id=product_id)
        quantity_reviews = product.reviews.count()
        total_rating = product.reviews.aggregate(Sum("rating"))["rating__sum"]

        with transaction.atomic():
            product.quantity_reviews = quantity_reviews
            product.rating = round(total_rating / quantity_reviews, 2) if quantity_reviews else 0
            product.save()
