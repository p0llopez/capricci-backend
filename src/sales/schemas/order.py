from datetime import datetime
from decimal import Decimal
from uuid import UUID

from ninja import ModelSchema, Schema

from src.sales.models import Order

from .order_item import CreateOrderItemSchema, OrderItemSchema


class CreateOrderSchema(ModelSchema):
    order_items: list[CreateOrderItemSchema] = []
    points_used: int

    class Meta:
        model = Order
        fields = (
            "payment_status",
            "shipping_price",
            "status",
        )


class OrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = "__all__"


class OrderWithItemsSchema(Schema):
    order_items: list[OrderItemSchema]
    id: UUID
    total_price: Decimal
    status: str
    created_at: datetime
    discount: Decimal
    items_price: Decimal
    shipping_price: Decimal
    status: str
    payment_status: str


class BasicOrderSchema(ModelSchema):
    class Meta:
        model = Order
        fields = ("id", "total_price", "status", "created_at")
