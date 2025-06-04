import requests
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from django.contrib.auth import get_user_model
import logging

logger = logging.getLogger(__name__)
User = get_user_model()


class ConditionalTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        if getattr(settings, 'API_AUTH_DISABLED', False):
            return None
        return super().authenticate(request)


class IdentityProviderSessionAuthentication(SessionAuthentication):
    """
    Custom authentication that validates session against CieloIdentityProvider
    """
    
    def authenticate(self, request):
        # First try standard session authentication
        user_auth_tuple = super().authenticate(request)
        
        if user_auth_tuple is None:
            # No local session, try to validate with Identity Provider
            return self.validate_with_identity_provider(request)
        
        # We have a local session, validate it with Identity Provider
        _, _ = user_auth_tuple  # user, auth
        if self.is_session_valid_with_identity_provider(request):
            return user_auth_tuple
        else:
            # Session is invalid with Identity Provider, clear local session
            request.session.flush()
            return None

    def validate_with_identity_provider(self, request):
        """
        Validate session with the Identity Provider
        """
        try:
            identity_url = getattr(settings, 'IDENTITY_SESSION_ENDPOINT', 
                                 'http://identity.cielo.test/session/')
            
            # Forward the session cookie to Identity Provider
            cookies = {}
            session_cookie_name = getattr(settings, 'SESSION_COOKIE_NAME', 'cielo_sessionid')
            if session_cookie_name in request.COOKIES:
                cookies[session_cookie_name] = request.COOKIES[session_cookie_name]
            
            response = requests.get(identity_url, cookies=cookies, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('authenticated', False):
                    # Session is valid, create a minimal authenticated user
                    # In a full implementation, you might want to fetch user data
                    user = User(username='authenticated_user')
                    return (user, None)
            
            return None
            
        except Exception as e:
            logger.error(f"Error validating session with Identity Provider: {e}")
            return None

    def is_session_valid_with_identity_provider(self, request):
        """
        Check if the current session is valid with Identity Provider
        """
        try:
            identity_url = getattr(settings, 'IDENTITY_SESSION_ENDPOINT', 
                                 'http://identity.cielo.test/session/')
            
            cookies = {}
            session_cookie_name = getattr(settings, 'SESSION_COOKIE_NAME', 'cielo_sessionid')
            if session_cookie_name in request.COOKIES:
                cookies[session_cookie_name] = request.COOKIES[session_cookie_name]
            
            response = requests.get(identity_url, cookies=cookies, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                return data.get('authenticated', False)
            
            return False
            
        except Exception as e:
            logger.error(f"Error checking session with Identity Provider: {e}")
            return False