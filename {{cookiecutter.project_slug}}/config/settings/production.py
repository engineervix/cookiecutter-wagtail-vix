"""See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/"""

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
