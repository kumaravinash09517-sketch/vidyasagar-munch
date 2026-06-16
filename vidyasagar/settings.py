import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cloudinary_storage',
    'munch', # आपका ऐप नाम
]

# Cloudinary Config
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudStorage'

# बाकि सेटिंग्स (Database, etc)
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# यहाँ से अपना बाकी का ओरिजिनल सेटिंग्स कोड जोड़ें...
