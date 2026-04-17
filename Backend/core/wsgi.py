"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# This will run once when the Vercel function starts
try:
    print("Running auto-migration and seeding on Vercel...")
    call_command('migrate', interactive=False)
    
    # Optional: Run seeding if database is completely empty
    from store.models import Product
    if Product.objects.count() == 0:
        print("Seeding initial products...")
        import subprocess
        subprocess.run(["python", "seed_final_v7.py"], check=True)
except Exception as e:
    print(f"Database setup error: {e}")

application = get_wsgi_application()
app = application
