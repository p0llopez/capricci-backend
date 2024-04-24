from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.customer.models import Customer
from src.customer.schemas import CreateCustomerSchema, CustomerSchema, UpdateCustomerSchema


@api_controller("/customers")
class CustomerController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_customer(self, payload: CreateCustomerSchema):
        try:
            customer = payload.create()
            return 201, {"id": customer.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("", response=[(200, list[CustomerSchema])], url_name="list")
    def list_customers(self):
        return 200, Customer.objects.all()

    @route.get("/{uuid:customer_id}", response=[(200, CustomerSchema)], url_name="retrieve")
    def retrieve_customer(self, customer_id: UUID):
        return 200, self.get_object_or_exception(Customer, id=customer_id, error_message="Customer not found")

    @route.put("/{uuid:customer_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_customer(self, customer_id: UUID, payload: UpdateCustomerSchema):
        customer_instance = self.get_object_or_exception(Customer, id=customer_id, error_message="Customer not found")
        customer = payload.update(instance=customer_instance)
        return 200, {"id": customer.id}

    @route.delete("/{uuid:customer_id}", response=[(204, None)], url_name="delete")
    def delete_customer(self, customer_id: UUID):
        customer = self.get_object_or_exception(Customer, id=customer_id, error_message="Customer not found")
        customer.delete()
        return 204, None
