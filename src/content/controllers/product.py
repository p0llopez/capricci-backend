from uuid import UUID

from django.db.models import Q
from ninja_extra import api_controller, route

from src.content.models import Product
from src.content.schemas import ProductSchema
from src.crm.schemas import ReviewSchema


@api_controller("/products")
class ProductController:
    @route.get("", response=[(200, list[ProductSchema])], url_name="list")
    def list_products(self, search: str | None = None):
        queryset = Product.objects.all()
        if search:
            queryset = queryset.filter(Q(name__icontains=search) | Q(brand__icontains=search))
        return 200, queryset

    @route.get("/{uuid:product_id}", response=[(200, ProductSchema)], url_name="retrieve")
    def retrieve_product(self, product_id: UUID):
        return 200, self.get_object_or_exception(Product, id=product_id, error_message="Product not found")

    @route.get("/{uuid:product_id}/reviews", response=[(200, list[ReviewSchema])], url_name="list_reviews")
    def list_reviews(self, product_id: UUID):
        product = self.get_object_or_exception(Product, id=product_id, error_message="Product not found")
        return 200, product.reviews.all()
