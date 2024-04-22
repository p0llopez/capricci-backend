from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class CustomerConfig(AppConfig):
    name = "src.customer"
    verbose_name = gettext_lazy("Customer")
