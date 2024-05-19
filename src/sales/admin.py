from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "status", "payment_status")
    search_fields = ("id", "user__first_name", "user__last_name", "user__email")
    list_filter = ("status", "payment_status")
    autocomplete_fields = ("user",)
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
