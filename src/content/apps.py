import logging

from django.apps import AppConfig
from django.utils.translation import gettext_lazy

logger = logging.getLogger(__name__)


class ContentConfig(AppConfig):
    name = "src.content"
    verbose_name = gettext_lazy("Content")

    def ready(self) -> None:
        try:
            from .signals import receivers  # noqa F401

        except ImportError:
            logger.error("Cannot import signals from Review app.")
