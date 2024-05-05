from src.commons.schemas import BaseModelSchema
from src.review.models import Review


class ReviewSchema(BaseModelSchema):
    class Config:
        model = Review
        include = "__all__"
        depth = 2


class CreateReviewSchema(BaseModelSchema):
    class Config:
        model = Review
        include = "__all__"
        exclude = ("id", "created_at", "updated_at", "rating")


class UpdateReviewSchema(BaseModelSchema):
    class Config:
        model = Review
        include = "__all__"
        exclude = ("id", "created_at", "updated_at", "rating")
        optional = ("__all__",)
