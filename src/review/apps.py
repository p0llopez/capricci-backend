import logging

from django.apps import AppConfig
from django.utils.translation import gettext_lazy

logger = logging.getLogger(__name__)


class ReviewConfig(AppConfig):
    name = "src.review"
    verbose_name = gettext_lazy("Review")

    # def ready(self) -> None:
    #     try:
    #         from .signals import receivers  # F401
    #
    #     except ImportError:
    #         logger.error("Cannot import signals from Review app.")
