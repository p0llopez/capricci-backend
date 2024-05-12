from django.db.models.signals import post_delete
from django.dispatch import receiver

from src.content.models import Product


@receiver(post_delete, sender=Product)
def remove_image_from_s3(instance: Product, **kwargs):
    instance.image.delete(save=False)
