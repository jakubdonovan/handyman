from src.settings.components.common import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "[::1]",
    ".ngrok.io"
    ]

INSTALLED_APPS += ["livereload"]

MIDDLEWARE += {
    "whitenoise.middleware.WhiteNoiseMiddleware",
}
