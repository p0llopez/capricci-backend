from datetime import datetime
from uuid import UUID

from ninja import ModelSchema, Schema

from src.content.schemas import BasicProductSchema
from src.crm.models import Review
from src.iam.schemas.user import BasicUserSchema


class ReviewSchema(Schema):
    id: UUID
    user: BasicUserSchema
    rating: int
    comment: str
    product: BasicProductSchema
    created_at: datetime
    updated_at: datetime


class CreateReviewSchema(ModelSchema):
    class Meta:
        model = Review
        exclude = (
            "id",
            "created_at",
            "updated_at",
        )


class UpdateReviewSchema(ModelSchema):
    class Meta:
        model = Review
        exclude = ("id", "created_at", "updated_at", "rating")
        fields_optional = "__all__"
