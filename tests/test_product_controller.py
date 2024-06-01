import pytest
from django.test import TestCase
from ninja_extra.testing import TestClient

from src.content.controllers import ProductController
from src.content.models import Product
from src.crm.models import Review


@pytest.mark.django_db()
class ProductControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient(ProductController)
        self.product1 = Product.objects.create(
            name="Product 1",
            brand="Brand 1",
            price=100.00,
            stock=10,
            presentation=1,
            presentation_format="unit",
            description="Product 1 description",
            image="product1.jpg",
        )
        self.product2 = Product.objects.create(
            name="Product 2",
            brand="Brand 2",
            price=200.00,
            stock=20,
            presentation=1,
            presentation_format="unit",
            description="Product 2 description",
            image="product2.jpg",
        )

        self.review1 = Review.objects.create(product=self.product1, rating=5, comment="Great product!")
        self.review2 = Review.objects.create(product=self.product1, rating=1, comment="Terrible product!")

    def test_list_products(self):
        # Test the list_products endpoint.
        response = self.client.get("")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_retrieve_product(self):
        # Test the retrieve_product endpoint.
        response = self.client.get(f"{self.product1.id}")
        assert response.status_code == 200
        assert response.json()["name"] == self.product1.name

    def test_list_reviews(self):
        # Test the list_reviews endpoint.
        response = self.client.get(f"{self.product1.id}/reviews")
        assert response.status_code == 200
        assert len(response.json()) == 2

        for review in response.json():
            if review["id"] == str(self.review1.id):
                assert review["comment"] == self.review1.comment
                assert review["rating"] == self.review1.rating

            elif review["id"] == str(self.review2.id):
                assert review["comment"] == self.review2.comment
                assert review["rating"] == self.review2.rating

            else:
                self.fail("Unexpected review")
