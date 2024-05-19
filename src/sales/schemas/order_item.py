from uuid import UUID

from ninja import ModelSchema

from src.content.schemas import BasicProductSchema
from src.sales.models import OrderItem


class CreateOrderItemSchema(ModelSchema):
    product_id: UUID

    class Meta:
        model = OrderItem
        exclude = ("id", "created_at", "updated_at", "order", "product")


class OrderItemSchema(ModelSchema):
    product: BasicProductSchema

    class Meta:
        model = OrderItem
        exclude = ("order",)
