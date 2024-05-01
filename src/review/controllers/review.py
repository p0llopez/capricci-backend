from uuid import UUID

from ninja_extra import api_controller, route

from src.commons.schemas import DetailsSchema, IdSchema
from src.review.models import Review
from src.review.schemas import CreateReviewSchema, ReviewSchema, UpdateReviewSchema


@api_controller("/reviews")
class ReviewController:
    @route.get("", response=[(200, list[ReviewSchema])], url_name="list")
    def list_reviews(self):
        return 200, Review.objects.all()

    @route.get("/{uuid:review_id}", response=[(200, ReviewSchema)], url_name="retrieve")
    def retrieve_review(self, review_id: UUID):
        return 200, self.get_object_or_exception(Review, id=review_id, error_message="Review not found")

    @route.post("", response=[(201, IdSchema), (400, DetailsSchema)], url_name="create")
    def create_review(self, payload: CreateReviewSchema):
        try:
            instance = payload.create()
            return 201, {"id": instance.id}
        except Exception as e:
            return 400, {"details": str(e)}

    @route.put("/{uuid:review_id}", response=[(200, IdSchema), (400, DetailsSchema)], url_name="update")
    def update_review(self, review_id: UUID, payload: UpdateReviewSchema):
        instance = self.get_object_or_exception(Review, id=review_id, error_message="Review not found")
        updated_instance = payload.update(instance=instance)
        return 200, {"id": updated_instance.id}

    @route.delete("/{uuid:review_id}", response=[(204, None)], url_name="delete")
    def delete_review(self, review_id: UUID):
        instance = self.get_object_or_exception(Review, id=review_id, error_message="Review not found")
        instance.delete()
        return 204, None
