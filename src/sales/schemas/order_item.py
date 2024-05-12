from ninja import ModelSchema

from src.sales.models import OrderItem


class OrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem
        fields = "__all__"


class CreateOrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem
        exclude = ("id", "created_at", "updated_at")


class UpdateOrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem
        exclude = ("id", "created_at", "updated_at")
        fields_optional = "__all__"
