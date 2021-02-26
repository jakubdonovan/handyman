import environ

DEBUG = False

ALLOWED_HOSTS = [
    environ("DOMAIN_NAME"),
]
