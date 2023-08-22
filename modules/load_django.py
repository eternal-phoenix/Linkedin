import sys
import os
import django
from pathlib import Path

sys.path.append(f'{Path(__file__).resolve().parent.parent}')
os.environ['DJANGO_SETTINGS_MODULE'] = 'parser.settings'
django.setup()