from .local import *  # noqa: F403
from .local import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("PGDATABASE"),
        "USER": env("PGUSER"),
        "PASSWORD": env("PGPASSWORD"),
        "HOST": env("PGHOST"),
        "PORT": env("PGPORT", default=5432),
        "OPTIONS": {
            "sslmode": "allow",
        },
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}

# aws settings
# https://medium.com/@hrushi669/file-storage-with-aws-s3-buckets-upload-for-the-django-project-50ea7208c4b1
AWS_ACCESS_KEY_ID = env("R2_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = env("R2_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = env("R2_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("R2_ENDPOINT_URL")
AWS_S3_SIGNATURE_VERSION = "s3v4"

# Static files (CSS, JavaScript, images)
STATIC_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{STATIC_LOCATION}/"
STATICFILES_STORAGE = "config.storages.StaticStorage"

# Media files
MEDIA_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "config.storages.MediaStorage"
