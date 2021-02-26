from src.settings import env

DEBUG = False

ALLOWED_HOSTS = [
    env("DOMAIN_NAME"),
]
