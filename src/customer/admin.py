from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.template.response import TemplateResponse

from .models import Address, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone_number")
    search_fields = ("first_name", "last_name", "email", "phone_number")
    ordering = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def changelist_view(self, request, extra_context=None) -> TemplateResponse:
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Customers"
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("__str__", "customer")
    search_fields = ("address", "city", "country", "zip_code", "customer__first_name", "customer__last_name")
    list_filter = ("city", "country", "zip_code")
    autocomplete_fields = ("customer",)
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Address]:
        return super().get_queryset(request).select_related("customer")

    def changelist_view(self, request, extra_context=None) -> TemplateResponse:
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Addresses"
        return super().changelist_view(request, extra_context=extra_context)
