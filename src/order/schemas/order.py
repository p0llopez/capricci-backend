from src.commons.schemas import BaseModelSchema
from src.order.models import Order


class OrderSchema(BaseModelSchema):
    class Config:
        model = Order
        include = "__all__"


class CreateOrderSchema(BaseModelSchema):
    class Config:
        model = Order
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")


class UpdateOrderSchema(BaseModelSchema):
    class Config:
        model = Order
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")
        optional = ("__all__",)
