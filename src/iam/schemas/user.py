from ninja import ModelSchema

from src.iam.models import User


class CreateUserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password")


class UserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "points")


class LoginUserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("email", "password")


class BasicUserSchema(ModelSchema):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")
