from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from src.content.use_cases import UpdateRatingAndReviewsNumberUseCase
from src.crm.models import Review


@receiver((post_save, post_delete), sender=Review)
def update_rating_and_num_reviews(instance: Review, **kwargs):
    UpdateRatingAndReviewsNumberUseCase()(instance.product_id)
