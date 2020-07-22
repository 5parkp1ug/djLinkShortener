from backend.dlsAPI.settings import *
import tempfile

MEDIA_ROOT = tempfile.mkdtemp()
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'