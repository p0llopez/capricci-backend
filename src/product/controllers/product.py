from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.product.models import Product
from src.product.schemas import CreateProductSchema, ProductSchema, UpdateProductSchema


@api_controller("/products")
class ProductController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_product(self, payload: CreateProductSchema):
        try:
            instance = payload.create()
            return 201, {"id": instance.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("", response=[(200, list[ProductSchema])], url_name="list")
    def list_products(self):
        return 200, Product.objects.all()

    @route.get("/{uuid:product_id}", response=[(200, ProductSchema)], url_name="retrieve")
    def retrieve_product(self, product_id: UUID):
        return 200, self.get_object_or_exception(Product, id=product_id, error_message="Product not found")

    @route.put("/{uuid:product_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_product(self, product_id: UUID, payload: UpdateProductSchema):
        instance = self.get_object_or_exception(Product, id=product_id, error_message="Product not found")
        updated_instance = payload.update(instance=instance)
        return 200, {"id": updated_instance.id}

    @route.delete("/{uuid:product_id}", response=[(204, None)], url_name="delete")
    def delete_product(self, product_id: UUID):
        instance = self.get_object_or_exception(Product, id=product_id, error_message="Product not found")
        instance.delete()
        return 204, None
