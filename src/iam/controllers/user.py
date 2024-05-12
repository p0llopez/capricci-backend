from urllib.parse import unquote

from django.contrib.auth.hashers import make_password
from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.iam.models import User
from src.iam.schemas import CreateUserSchema


@api_controller("/users")
class UserController:
    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_user(self, payload: CreateUserSchema):
        try:
            payload.email = payload.email.lower()
            payload.first_name = payload.first_name.capitalize()
            payload.last_name = payload.last_name.capitalize()
            payload.password = make_password(payload.password)
            user_dict = payload.dict()
            user_dict.update({"username": payload.email})
            user = User.objects.create(**user_dict)
            return 201, {"id": user.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.get("/exists/{email}", response=[(200, bool)], url_name="exists")
    def check_user_exists(self, email: str):
        decoded_email = unquote(email)
        return 200, User.objects.filter(email=decoded_email, is_staff=False).exists()
