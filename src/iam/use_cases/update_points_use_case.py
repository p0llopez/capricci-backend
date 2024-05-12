from uuid import UUID

from src.iam.models import User


class UpdatePointsUseCase:
    def __call__(self, user_id: UUID, points_to_add: int, points_to_remove: int):
        user = User.objects.get(id=user_id)
        user.points += points_to_add
        user.points -= points_to_remove
        user.save()
        return user.points
