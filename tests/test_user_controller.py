import pytest
from django.test import TestCase
from ninja_extra.testing import TestClient

from src.content.models import Product
from src.crm.models import Review
from src.iam.controllers import UserController
from src.iam.models import User
from src.sales.models import Order, OrderItem
from tests.utils import get_authenticated_header_for_user


@pytest.mark.django_db()
class UserControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient(UserController)
        self.user = User.objects.create(
            email="email@example.com",
            first_name="John",
            last_name="Doe",
            password="password",
            is_staff=False,
        )
        self.order = Order.objects.create(
            discount=0,
            items_price=100,
            payment_status="pending",
            shipping_price=10,
            status="pending",
            total_price=110,
            user=self.user,
        )
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
        self.order_item = OrderItem.objects.create(
            order_id=self.order.id,
            product_id=self.product.id,
            quantity=1,
            unit_price=100.00,
        )
        self.review = Review.objects.create(
            rating=5,
            comment="Great product!",
            product_id=self.product.id,
            user=self.user,
        )

    def test_create_user(self):
        # Test the create_user endpoint.
        response = self.client.post(
            "",
            json={
                "email": "email2@example.com",
                "first_name": "Jane",
                "last_name": "Doe",
                "password": "password",
            },
        )

        assert response.status_code == 201
        assert User.objects.count() == 2

    def test_check_user_exists(self):
        # Test the check_user_exists endpoint.
        response = self.client.get(f"/exists/{self.user.email}")
        assert response.status_code == 200
        assert response.json() is True

        response = self.client.get("/exists/non-existing-mail@example.com")
        assert response.status_code == 200
        assert response.json() is False

    def test_retrieve_user(self):
        # Test the retrieve_user endpoint.
        header = get_authenticated_header_for_user(self.user)
        response = self.client.get("/me", headers=header)

        assert response.status_code == 200
        assert response.json()["id"] == str(self.user.id)

    def test_list_orders(self):
        # Test the list_orders endpoint.
        header = get_authenticated_header_for_user(self.user)
        response = self.client.get("/me/orders", headers=header)

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == str(self.order.id)

    def test_retrieve_order(self):
        # Test the retrieve_order endpoint.
        header = get_authenticated_header_for_user(self.user)
        response = self.client.get(f"/me/orders/{self.order.id}", headers=header)

        assert response.status_code == 200
        assert response.json()["id"] == str(self.order.id)
        assert len(response.json()["order_items"]) == 1
        assert response.json()["order_items"][0]["id"] == str(self.order_item.id)

    def test_list_reviews(self):
        # Test the list_reviews endpoint.
        header = get_authenticated_header_for_user(self.user)
        response = self.client.get("/me/reviews", headers=header)

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == str(self.review.id)
