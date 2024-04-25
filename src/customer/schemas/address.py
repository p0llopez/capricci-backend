from src.commons.schemas import BaseModelSchema
from src.customer.models import Address


class AddressSchema(BaseModelSchema):
    class Config:
        model = Address
        include = "__all__"


class CreateAddressSchema(BaseModelSchema):
    class Config:
        model = Address
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")


class UpdateAddressSchema(BaseModelSchema):
    class Config:
        model = Address
        include = "__all__"
        exclude = ("id", "created_at", "updated_at")
        optional = ("__all__",)
