import logging
from io import BytesIO

import matplotlib.image as mpimg
from django.core.files.base import ContentFile
from django.core.management import BaseCommand
from faker import Faker
from randimage import get_random_image

from src.content.models import Product

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create N random products"

    @staticmethod
    def generate_random_image(name):
        # Generate a random image
        image = get_random_image((500, 500))

        # Convert the image to a file-like object
        with BytesIO() as buffer:
            mpimg.imsave(buffer, image, format="png")
            buffer.seek(0)
            return ContentFile(buffer.read(), f"{name}.png")

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="Number of products to create")

    def handle(self, **options):
        faker = Faker()
        number_of_products = options["n"]

        logger.info(f"Creating {number_of_products} random products")
        for i in range(number_of_products):
            logger.info(f"Creating product {i + 1}/{number_of_products}...")
            name = faker.word()

            Product.objects.create(
                brand=faker.company(),
                category=faker.word(),
                description=faker.paragraph(nb_sentences=5),
                image=self.generate_random_image(name),
                name=name,
                presentation=faker.random_int(min=1, max=100),
                presentation_format=faker.random_element(
                    elements=(
                        "mililitros",
                        "gramos",
                        "unidades",
                        "kilogramos",
                        "litros",
                    )
                ),
                price=faker.pydecimal(left_digits=2, right_digits=2, positive=True),
                stock=faker.random_int(min=1, max=100),
            )

        logger.info("Created all products")
