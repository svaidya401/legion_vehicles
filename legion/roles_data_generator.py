import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legion.settings')

import django
django.setup()

from user_app.models import Role

everyone_role, created = Role.objects.get_or_create(name = 'EVERYONE')

if created == True:
    everyone_role.save()
