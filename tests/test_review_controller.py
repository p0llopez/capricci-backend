import pytest
from django.test import TestCase
from ninja_extra.testing import TestClient

from src.content.models import Product
from src.crm.controllers import ReviewController
from src.crm.models import Review
from src.iam.models import User
from tests.utils import get_authenticated_header_for_user


@pytest.mark.django_db()
class ReviewControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient(ReviewController)
        self.product = Product.objects.create(
            name="Product 1",
            brand="Brand 1",
            price=100.00,
            stock=10,
            presentation=1,
            presentation_format="unit",
            description="Product 1 description",
            image="product1.jpg",
        )
        self.review1 = Review.objects.create(rating=5, comment="Great product!", product_id=self.product.id)
        self.review2 = Review.objects.create(rating=1, comment="Terrible product!", product_id=self.product.id)

        self.user = User.objects.create_user(username="user", password="password", email="email@example.com")
        self.authenticated_header = get_authenticated_header_for_user(self.user)

    def test_create_review(self):
        # Test the create_review endpoint.
        response = self.client.post(
            "",
            json={"rating": 4, "comment": "Good product!", "product_id": str(self.product.id)},
            headers=self.authenticated_header,
        )
        assert response.status_code == 201
        assert Review.objects.count() == 3

    def test_delete_review(self):
        # Test the delete_review endpoint.
        response = self.client.delete(f"{self.review1.id}", headers=self.authenticated_header)
        assert response.status_code == 204
        assert Review.objects.count() == 1
