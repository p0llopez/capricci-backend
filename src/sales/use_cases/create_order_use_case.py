from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from django.db import transaction

from src.iam.use_cases import UpdatePointsUseCase
from src.sales.models import Order, OrderItem


@dataclass
class OrderItemDTO:
    product_id: UUID
    quantity: int
    unit_price: Decimal


@dataclass
class CreateOrderUseCaseDTO:
    user_id: UUID
    points_used: int
    payment_status: str
    shipping_price: Decimal
    status: str
    order_items: list[OrderItemDTO]


class CreateOrderUseCase:
    @transaction.atomic
    def __call__(self, dto: CreateOrderUseCaseDTO):
        items_price = sum(item.quantity * item.unit_price for item in dto.order_items)
        discount = dto.points_used * Decimal("0.01")
        total_price = items_price + dto.shipping_price - discount
        order = Order.objects.create(
            user_id=dto.user_id,
            discount=discount,
            items_price=items_price,
            payment_status=dto.payment_status,
            shipping_price=dto.shipping_price,
            status=dto.status,
            total_price=total_price,
        )

        order_items = [
            OrderItem(
                order=order,
                product_id=item.product_id,
                quantity=item.quantity,
                unit_price=item.unit_price,
            )
            for item in dto.order_items
        ]
        OrderItem.objects.bulk_create(order_items)

        points_to_add = total_price * Decimal("0.1")
        UpdatePointsUseCase()(user_id=dto.user_id, points_to_add=points_to_add, points_to_remove=dto.points_used)

        return order.id
