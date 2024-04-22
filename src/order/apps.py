from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class OrderConfig(AppConfig):
    name = "src.order"
    verbose_name = gettext_lazy("Order")
