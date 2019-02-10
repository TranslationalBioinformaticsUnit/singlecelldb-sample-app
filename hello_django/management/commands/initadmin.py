__author__ = 'alberto.labarga@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand
from authentication.models import Account
from django.contrib.auth import User

class Command(BaseCommand):

    def handle(self, *args, **options):
    username = 'scooby'
    passwdord = 'singapur'
        email = 'alabargh@navarra.es'
        User.objects.create_superuser(username, email, password)
