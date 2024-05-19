from urllib.parse import unquote
from uuid import UUID

import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from ninja_extra import api_controller, route
from ninja_jwt.authentication import JWTAuth

from src.commons.schemas import DetailsSchema, IdSchema
from src.crm.models import Review
from src.crm.schemas import ReviewSchema
from src.iam.models import User
from src.iam.schemas import CreateUserSchema, UserSchema
from src.sales.models import Order
from src.sales.schemas import BasicOrderSchema, OrderWithItemsSchema


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

    @route.get("/me", response=[(200, UserSchema)], url_name="get", auth=JWTAuth())
    def retrieve_user(self):
        token = self.context.request.headers.get("Authorization").split(" ")[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        return 200, User.objects.get(id=user_id)

    @route.get("/me/orders", response=[(200, list[BasicOrderSchema])], url_name="list_orders", auth=JWTAuth())
    def list_orders(self):
        token = self.context.request.headers.get("Authorization").split(" ")[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        return 200, Order.objects.filter(user_id=user_id).order_by("-created_at")

    @route.get(
        "/me/orders/{uuid:order_id}",
        response=[(200, OrderWithItemsSchema), (404, DetailsSchema)],
        url_name="get",
        auth=JWTAuth(),
    )
    def retrieve_order(self, order_id: UUID):
        token = self.context.request.headers.get("Authorization").split(" ")[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        return 200, self.get_object_or_exception(Order, id=order_id, user_id=user_id, error_message="Order not found")

    @route.get("/me/reviews", response=[(200, list[ReviewSchema])], url_name="list_reviews", auth=JWTAuth())
    def list_reviews(self):
        token = self.context.request.headers.get("Authorization").split(" ")[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        return 200, Review.objects.filter(user_id=user_id).order_by("-created_at")
