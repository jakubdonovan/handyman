from src.utils import config

DEBUG = False

ALLOWED_HOSTS = [
    config("DOMAIN_NAME"),
]
