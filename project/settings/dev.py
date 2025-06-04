from .base import *

DEBUG = True

# Extend allowed hosts for development
ALLOWED_HOSTS.extend([".dev.viloforge.com", "azurebilling.dev.viloforge.com", "localhost", "127.0.0.1"])

# Session configuration - match Identity Provider
SESSION_COOKIE_DOMAIN = ".dev.viloforge.com"
SESSION_COOKIE_NAME = 'cielo_sessionid'
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_SAMESITE = 'None'  # None required for cross-origin HTTPS
SESSION_COOKIE_SECURE = True  # Required for HTTPS and SameSite=None
SESSION_COOKIE_HTTPONLY = False  # Allow JavaScript access for cross-origin
SESSION_SAVE_EVERY_REQUEST = True  # Ensure session persistence

# Use cache backend for session storage (should match Identity Provider)
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# CORS settings for cross-origin requests from frontend
CORS_ALLOW_CREDENTIALS = True  # Essential for cookie transmission
CORS_ALLOWED_ORIGINS = [
    "https://cielo.dev.viloforge.com",
    "https://identity.dev.viloforge.com",
    "https://billing.dev.viloforge.com",
    "https://azurebilling.dev.viloforge.com",
]
CORS_EXPOSE_HEADERS = ['Set-Cookie']  # Allow JS to see Set-Cookie header
CORS_PREFLIGHT_MAX_AGE = 86400  # Cache preflight requests for 24 hours

# Identity Provider configuration
IDENTITY_PROVIDER_BASE_URL = "https://identity.dev.viloforge.com"
IDENTITY_SESSION_ENDPOINT = f"{IDENTITY_PROVIDER_BASE_URL}/api/session/"
IDENTITY_CURRENT_USER_ENDPOINT = f"{IDENTITY_PROVIDER_BASE_URL}/api/users/me/"

# Secret key for development only
SECRET_KEY = 'django-insecure-change-me'
