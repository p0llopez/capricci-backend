from ninja import ModelSchema

from src.content.models import Product


class ProductSchema(ModelSchema):
    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSchema(ModelSchema):
    class Meta:
        model = Product
        exclude = ("id", "created_at", "updated_at", "rating", "quantity_reviews")


class UpdateProductSchema(ModelSchema):
    class Meta:
        model = Product
        exclude = ("id", "created_at", "updated_at", "rating", "quantity_reviews")
        fields_optional = "__all__"
