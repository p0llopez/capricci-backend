from src.commons.schemas import BaseModelSchema
from src.order.models import OrderItem


class OrderItemSchema(BaseModelSchema):
    class Config:
        model = OrderItem
        include = "__all__"


class CreateOrderItemSchema(BaseModelSchema):
    class Config:
        model = OrderItem
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")


class UpdateOrderItemSchema(BaseModelSchema):
    class Config:
        model = OrderItem
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")
        optional = ("__all__",)
