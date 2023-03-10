import os
import dj_database_url

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
 'default': dj_database_url.config(conn_max_age=500)
}

SECRET_KEY = os.getenv('SECRET_KEY', 'REPLACE_ME')

INSTALLED_APPS = ['datacenter']

DEBUG = os.getenv('DEBUG', False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', ['localhost', '127.0.0.1'])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
