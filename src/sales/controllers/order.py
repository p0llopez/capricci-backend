from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.sales.schemas import CreateOrderSchema
from src.sales.use_cases import CreateOrderUseCase, CreateOrderUseCaseDTO, OrderItemDTO


@api_controller("/orders")
class OrderController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_order(self, payload: CreateOrderSchema):
        try:
            order_items = [
                OrderItemDTO(
                    product_id=item.product_id,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                )
                for item in payload.order_items
            ]
            dto = CreateOrderUseCaseDTO(
                user_id=payload.user,
                points_used=payload.points_used,
                payment_status=payload.payment_status,
                shipping_price=payload.shipping_price,
                status=payload.status,
                order_items=order_items,
            )
            order_id = CreateOrderUseCase()(dto)
            return 201, {"id": order_id}
        except Exception as e:
            return 400, {"details": str(e)}
