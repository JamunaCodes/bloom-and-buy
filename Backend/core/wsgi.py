import os
import sys

# Ultimate Path Injection: Hardcode the paths to ensures absolute discovery
# This solves Vercel's confusion about the directory structure
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    app = application
except Exception as e:
    # Minimalist fallback to show the error without any extra library dependencies
    import traceback
    error_trace = traceback.format_exc()
    def app(environ, start_response):
        if environ.get('PATH_INFO') == '/api/health-check':
             start_response('200 OK', [('Content-Type', 'text/plain')])
             return [b"Python is working, but Django failed to start."]
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [f"BOOTSTRAP CRASH:\n\n{error_trace}".encode('utf-8')]
