from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.customer.models import Address
from src.customer.schemas import AddressSchema, CreateAddressSchema, UpdateAddressSchema


@api_controller("/addresses")
class AddressController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_address(self, payload: CreateAddressSchema):
        try:
            instance = payload.create()
            return 201, {"id": instance.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("", response=[(200, list[AddressSchema])], url_name="list")
    def list_addresses(self):
        return 200, Address.objects.all()

    @route.get("/{uuid:address_id}", response=[(200, AddressSchema)], url_name="retrieve")
    def retrieve_customer(self, address_id: UUID):
        return 200, self.get_object_or_exception(Address, id=address_id, error_message="Address not found")

    @route.put("/{uuid:address_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_customer(self, address_id: UUID, payload: UpdateAddressSchema):
        instance = self.get_object_or_exception(Address, id=address_id, error_message="Address not found")
        updated_instance = payload.update(instance=instance)
        return 200, {"id": updated_instance.id}

    @route.delete("/{uuid:address_id}", response=[(204, None)], url_name="delete")
    def delete_customer(self, address_id: UUID):
        instance = self.get_object_or_exception(Address, id=address_id, error_message="Address not found")
        instance.delete()
        return 204, None
