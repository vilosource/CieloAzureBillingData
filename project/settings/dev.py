from .base import *

DEBUG = True

# Extend allowed hosts for development
ALLOWED_HOSTS.extend([".cielo.test", "azurebilling.cielo.test", "localhost", "127.0.0.1"])

# Session configuration - match Identity Provider
SESSION_COOKIE_DOMAIN = ".cielo.test"
SESSION_COOKIE_NAME = 'cielo_sessionid'
SESSION_COOKIE_PATH = "/"
SESSION_COOKIE_SAMESITE = None  # Allow cross-site requests
SESSION_COOKIE_SECURE = False  # False for development (True for production)
SESSION_COOKIE_HTTPONLY = False  # False for debugging (True for production)
SESSION_SAVE_EVERY_REQUEST = True  # Ensure session persistence

# Use cache backend for session storage (should match Identity Provider)
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# CORS settings for cross-origin requests from frontend
CORS_ALLOW_CREDENTIALS = True  # Essential for cookie transmission
CORS_ALLOWED_ORIGINS = [
    "http://cielo.test",
    "http://localhost:8001",
    "http://identity.cielo.test",
    "http://localhost:8002",
]
CORS_EXPOSE_HEADERS = ['Set-Cookie']  # Allow JS to see Set-Cookie header
CORS_PREFLIGHT_MAX_AGE = 86400  # Cache preflight requests for 24 hours

# Identity Provider configuration
IDENTITY_PROVIDER_BASE_URL = "http://identity.cielo.test"
IDENTITY_SESSION_ENDPOINT = f"{IDENTITY_PROVIDER_BASE_URL}/session/"
IDENTITY_CURRENT_USER_ENDPOINT = f"{IDENTITY_PROVIDER_BASE_URL}/current-user/"

# Secret key for development only
SECRET_KEY = 'django-insecure-change-me'
