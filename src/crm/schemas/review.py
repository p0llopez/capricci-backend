from ninja import ModelSchema

from src.crm.models import Review


class ReviewSchema(ModelSchema):
    class Meta:
        model = Review
        fields = "__all__"


class CreateReviewSchema(ModelSchema):
    class Meta:
        model = Review
        exclude = ("id", "created_at", "updated_at", "rating")


class UpdateReviewSchema(ModelSchema):
    class Meta:
        model = Review
        exclude = ("id", "created_at", "updated_at", "rating")
        fields_optional = "__all__"
