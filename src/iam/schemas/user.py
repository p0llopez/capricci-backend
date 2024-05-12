from ninja import ModelSchema

from src.iam.models import User


class CreateUserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ("password",)


class LoginUserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("email", "password")
