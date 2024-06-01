from ninja_jwt.tokens import RefreshToken

from src.iam.models import User


def get_authenticated_header_for_user(user: User) -> dict:
    refresh_token = RefreshToken.for_user(user)
    access_token = refresh_token.access_token
    return {"Authorization": f"Bearer {access_token}"}
