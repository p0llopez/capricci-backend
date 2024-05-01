import logging

from django.core.management import BaseCommand
from faker import Faker

from src.product.models import Product
from src.review.models import Review

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create N random reviews"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="Number of reviews to create")

    def handle(self, **options):
        faker = Faker()
        number_of_reviews = options["n"]

        for product in Product.objects.all():
            for _ in range(number_of_reviews):
                Review.objects.create(
                    product=product,
                    rating=faker.random_int(min=0, max=5),
                    comment=faker.paragraph(nb_sentences=2),
                    customer=None,
                )
