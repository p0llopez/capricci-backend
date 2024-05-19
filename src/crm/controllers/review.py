from uuid import UUID

import jwt
from django.conf import settings
from ninja_extra import api_controller, route
from ninja_jwt.authentication import JWTAuth

from src.commons.schemas import DetailsSchema
from src.crm.models import Review
from src.crm.schemas import CreateReviewSchema


@api_controller("/reviews")
class ReviewController:
    @route.post("", response=[(201, None), (404, DetailsSchema)], url_name="create", auth=JWTAuth())
    def create_review(self, payload: CreateReviewSchema):
        token = self.context.request.headers.get("Authorization").split(" ")[1]
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        Review.objects.create(user_id=user_id, product_id=payload.product, **payload.dict(exclude={"product"}))
        return 201, None

    @route.delete("/{uuid:review_id}", response=[(204, None), (404, DetailsSchema)], url_name="delete", auth=JWTAuth())
    def delete_review(self, review_id: UUID):
        review = self.get_object_or_exception(Review, id=review_id, error_message="Review not found")
        review.delete()
        return 204, None
