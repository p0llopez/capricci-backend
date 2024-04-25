from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.order.models import OrderItem
from src.order.schemas import CreateOrderItemSchema, OrderItemSchema, UpdateOrderItemSchema


@api_controller("/order_items")
class OrderItemController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_order_item(self, payload: CreateOrderItemSchema):
        try:
            instance = payload.create()
            return 201, {"id": instance.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("", response=[(200, list[OrderItemSchema])], url_name="list")
    def list_order_items(self):
        return 200, OrderItem.objects.all()

    @route.get("/{uuid:order_item_id}", response=[(200, OrderItemSchema)], url_name="retrieve")
    def retrieve_order_item(self, order_item_id: UUID):
        return 200, self.get_object_or_exception(OrderItem, id=order_item_id, error_message="OrderItem not found")

    @route.put("/{uuid:order_item_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_order_item(self, order_item_id: UUID, payload: UpdateOrderItemSchema):
        instance = self.get_object_or_exception(OrderItem, id=order_item_id, error_message="OrderItem not found")
        updated_instance = payload.update(instance=instance)
        return 200, {"id": updated_instance.id}

    @route.delete("/{uuid:order_item_id}", response=[(204, None)], url_name="delete")
    def delete_order_item(self, order_item_id: UUID):
        instance = self.get_object_or_exception(OrderItem, id=order_item_id, error_message="OrderItem not found")
        instance.delete()
        return 204, None
