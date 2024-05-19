from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class SalesConfig(AppConfig):
    name = "src.sales"
    verbose_name = gettext_lazy("Sales")
