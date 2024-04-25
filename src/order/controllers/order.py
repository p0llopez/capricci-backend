from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.order.models import Order
from src.order.schemas import CreateOrderSchema, OrderSchema, UpdateOrderSchema


@api_controller("/orders")
class OrderController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_order(self, payload: CreateOrderSchema):
        try:
            instance = payload.create()
            return 201, {"id": instance.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("", response=[(200, list[OrderSchema])], url_name="list")
    def list_orders(self):
        return 200, Order.objects.all()

    @route.get("/{uuid:order_id}", response=[(200, OrderSchema)], url_name="retrieve")
    def retrieve_customer(self, order_id: UUID):
        return 200, self.get_object_or_exception(Order, id=order_id, error_message="Order not found")

    @route.put("/{uuid:order_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_customer(self, order_id: UUID, payload: UpdateOrderSchema):
        instance = self.get_object_or_exception(Order, id=order_id, error_message="Order not found")
        updated_instance = payload.update(instance=instance)
        return 200, {"id": updated_instance.id}

    @route.delete("/{uuid:order_id}", response=[(204, None)], url_name="delete")
    def delete_customer(self, order_id: UUID):
        instance = self.get_object_or_exception(Order, id=order_id, error_message="Order not found")
        instance.delete()
        return 204, None
