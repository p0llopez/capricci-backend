from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class ProductConfig(AppConfig):
    name = "src.product"
    verbose_name = gettext_lazy("Product")
