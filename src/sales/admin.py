from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest
from django.template.response import TemplateResponse

from .models import Address, Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "status", "payment_status")
    search_fields = ("id", "user__first_name", "user__last_name", "user__email")
    list_filter = ("status", "payment_status")
    autocomplete_fields = ("user", "address")
    readonly_fields = ("created_at", "updated_at")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Orders"
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "unit_price")
    search_fields = ("id", "order__id", "product__name")
    list_filter = ("order__status", "order__payment_status")
    autocomplete_fields = ("order", "product")
    readonly_fields = ("created_at", "updated_at")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Order Items"
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("__str__", "user")
    search_fields = ("address", "city", "country", "zip_code", "user__first_name", "user__last_name")
    list_filter = ("city", "country", "zip_code")
    autocomplete_fields = ("user",)
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request: HttpRequest) -> QuerySet[Address]:
        return super().get_queryset(request).select_related("user", "order")

    def changelist_view(self, request, extra_context=None) -> TemplateResponse:
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Addresses"
        return super().changelist_view(request, extra_context=extra_context)
