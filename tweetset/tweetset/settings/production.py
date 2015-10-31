from .base import *
from .passwords import *
import os

# from production
# ALLOWED_HOSTS = ['tweetset.com','www.tweetset.com']
# STATIC_URL = 'http://static.tweetset.com/'


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEBUG_TOOLBAR = True

if DEBUG:
    # Show emails in the console during developement.
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG_TOOLBAR:
    INTERNAL_IPS = ('127.0.0.1',)
