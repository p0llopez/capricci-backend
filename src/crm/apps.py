import logging

from django.apps import AppConfig
from django.utils.translation import gettext_lazy

logger = logging.getLogger(__name__)


class CrmConfig(AppConfig):
    name = "src.crm"
    verbose_name = gettext_lazy("Crm")

    # def ready(self) -> None:
    #     try:
    #         from .signals import receivers  # F401
    #
    #     except ImportError:
    #         logger.error("Cannot import signals from Review app.")
