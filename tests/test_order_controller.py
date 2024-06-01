import pytest
from django.test import TestCase
from ninja_extra.testing import TestClient

from src.content.models import Product
from src.iam.models import User
from src.sales.controllers import OrderController
from src.sales.models import Order
from tests.utils import get_authenticated_header_for_user


@pytest.mark.django_db()
class OrderControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient(OrderController)
        self.user = User.objects.create(
            email="user@example.com",
            first_name="John",
            last_name="Doe",
            password="password",
            is_staff=False,
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

    def test_create_order(self):
        # Test the create_order endpoint.
        body = {
            "order_items": [
                {
                    "product_id": str(self.product.id),
                    "quantity": 1,
                    "unit_price": 100.00,
                }
            ],
            "points_used": 0,
            "payment_status": "pending",
            "shipping_price": 10.00,
            "status": "pending",
        }

        response = self.client.post(
            "",
            json=body,
            headers=get_authenticated_header_for_user(self.user),
        )
        assert response.status_code == 201
        assert Order.objects.count() == 1
