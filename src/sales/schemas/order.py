from ninja import ModelSchema

from src.sales.models import Order


class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = "__all__"


class CreateOrderSchema(ModelSchema):
    class Meta:
        model = Order
        exclude = ("id", "created_at", "updated_at")


class UpdateOrderSchema(ModelSchema):
    class Meta:
        model = Order
        exclude = ("id", "created_at", "updated_at")
        fields_optional = "__all__"
