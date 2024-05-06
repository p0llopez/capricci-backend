from uuid import UUID

from ninja_extra import api_controller, route
from ninja_extra.searching import Searching, searching

from src.product.models import Product
from src.product.schemas import ProductSchema
from src.review.schemas import ReviewSchema


@api_controller("/products")
class ProductController:
    @route.get("", response=[(200, list[ProductSchema])], url_name="list")
    @searching(Searching, search_fields=["@name", "@brand"])
    def list_products(self):
        return 200, Product.objects.all()

    @route.get("/{uuid:product_id}", response=[(200, ProductSchema)], url_name="retrieve")
    def retrieve_product(self, product_id: UUID):
        return 200, self.get_object_or_exception(Product, id=product_id, error_message="Product not found")

    @route.get("/{uuid:product_id}/reviews", response=[(200, list[ReviewSchema])], url_name="list_reviews")
    def list_reviews(self, product_id: UUID):
        product = self.get_object_or_exception(Product, id=product_id, error_message="Product not found")
        return 200, product.reviews.all()
