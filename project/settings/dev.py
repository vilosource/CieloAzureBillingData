from .base import *

DEBUG = True

# Development session cookie configuration
SESSION_COOKIE_DOMAIN = ".cielo.test"
SESSION_COOKIE_PATH = "/"

# Allow local hosts
ALLOWED_HOSTS = [".cielo.test", "localhost", "127.0.0.1"]

# Secret key for development only
SECRET_KEY = 'django-insecure-change-me'
