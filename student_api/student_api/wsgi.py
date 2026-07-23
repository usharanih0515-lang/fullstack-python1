"""
WSGI config for student_api project.
"""

import os
import sys
from pathlib import Path

# Ensure student_api root is in sys.path for Vercel Serverless Function imports
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_api.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application
