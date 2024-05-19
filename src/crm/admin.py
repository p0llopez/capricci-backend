from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "rating", "comment", "user")
    list_filter = ("product", "rating", "user")
    search_fields = ("product", "rating", "comment", "user")

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("product", "user")
