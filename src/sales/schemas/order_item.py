from ninja import ModelSchema

from src.sales.models import OrderItem


class CreateOrderItemSchema(ModelSchema):
    class Meta:
        model = OrderItem
        exclude = ("id", "created_at", "updated_at", "order")
