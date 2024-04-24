from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "price", "stock", "is_active")
    search_fields = ("id", "name", "brand", "category")
    list_filter = ("brand", "category", "is_active")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["title"] = "Manage Products"
        return super().changelist_view(request, extra_context=extra_context)
