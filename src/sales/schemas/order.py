from ninja import ModelSchema

from src.sales.models import Order

from .order_item import CreateOrderItemSchema


class CreateOrderSchema(ModelSchema):
    order_items: list[CreateOrderItemSchema] = []
    points_used: int

    class Meta:
        model = Order
        fields = (
            "user",
            "payment_status",
            "shipping_price",
            "status",
        )
