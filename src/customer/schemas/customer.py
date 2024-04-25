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
        optional = ("__all__",)


class CustomerSchema(BaseModelSchema):
    class Config:
        model = Customer
        include = "__all__"
        exclude = ("password",)
