from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class IamConfig(AppConfig):
    name = "src.iam"
    verbose_name = gettext_lazy("IAM")
