from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "comment", "customer")
    list_filter = ("product", "rating", "customer")
    search_fields = ("product", "rating", "comment", "customer")
