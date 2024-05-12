from ninja import ModelSchema

from src.sales.models import Address


class AddressSchema(ModelSchema):
    class Meta:
        model = Address
        fields = "__all__"


class CreateAddressSchema(ModelSchema):
    class Meta:
        model = Address
        exclude = ("id", "created_at", "updated_at")


class UpdateAddressSchema(ModelSchema):
    class Meta:
        model = Address
        exclude = ("id", "created_at", "updated_at")
        fields_optional = "__all__"
