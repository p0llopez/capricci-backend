from django.contrib import admin
from django.template.response import TemplateResponse

from src.iam.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
    )
    ordering = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("is_staff", "is_active")

    def changelist_view(self, request, extra_context=None) -> TemplateResponse:
        extra_context = extra_context or {}
        extra_context["title"] = "Manage users"
        return super().changelist_view(request, extra_context=extra_context)
