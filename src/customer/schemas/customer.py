from src.commons.schemas import BaseModelSchema
from src.customer.models import Customer


class CreateCustomerSchema(BaseModelSchema):
    class Config:
        model = Customer
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")


class UpdateCustomerSchema(BaseModelSchema):
    class Config:
        model = Customer
        include = "__all__"
        exclude = ("id", "created_at", "updated_at", "email", "password")
        optional = ("first_name", "last_name", "phone_number", "is_active", "points")


class CustomerSchema(BaseModelSchema):
    class Config:
        model = Customer
        include = "__all__"
        exclude = ("password",)
