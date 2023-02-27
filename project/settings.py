import os
import dj_database_url

from dotenv import load_dotenv

load_dotenv()

DATABASES = {
 'default': dj_database_url.config(conn_max_age=500)
}

SECRET_KEY = os.environ['SECRET_KEY']

INSTALLED_APPS = ['datacenter']

DEBUG = os.environ['DEBUG']

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['ALLOWED_HOSTS']


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
