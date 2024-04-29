from uuid import UUID

from ninja_extra import api_controller, route

from src.product.models import Product
from src.product.schemas import ProductSchema


@api_controller("/products")
class ProductController:
    @route.get("", response=[(200, list[ProductSchema])], url_name="list")
    def list_products(self):
        return 200, Product.objects.all()

    @route.get("/{uuid:product_id}", response=[(200, ProductSchema)], url_name="retrieve")
    def retrieve_product(self, product_id: UUID):
        return 200, self.get_object_or_exception(Product, id=product_id, error_message="Product not found")
