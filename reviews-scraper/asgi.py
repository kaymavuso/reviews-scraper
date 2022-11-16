"""
ASGI config for reviews-scraper job.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangojob.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reviews-scraper.settings')

application = get_asgi_application()
