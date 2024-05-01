from src.commons.schemas import BaseModelSchema
from src.product.models import Product


class ProductSchema(BaseModelSchema):
    class Config:
        model = Product
        include = "__all__"


class CreateProductSchema(BaseModelSchema):
    class Config:
        model = Product
        include = "__all__"
        exclude = ("id", "created_at", "updated_at", "rating", "quantity_reviews")


class UpdateProductSchema(BaseModelSchema):
    class Config:
        model = Product
        include = "__all__"
        exclude = ("id", "created_at", "updated_at", "rating", "quantity_reviews")
        optional = ("__all__",)
