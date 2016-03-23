"""
Django settings for ladynerds project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print PROJECT_ROOT
SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# Find templates in the same folder as settings.py.
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)



# TEMPLATE_DIRS = (
#     os.path.join(os.path.dirname(__file__), 'templates/'),
# )
print TEMPLATE_DIRS


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%r7-*w4evl10m(_0e%d5eq2cl=i&1($x*1%*pgp-$nzb6xi2zf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ladynerds'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ladynerds.urls'


# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
] 

WSGI_APPLICATION = 'ladynerds.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LOGIN_REDIRECT_URL = "/profile"
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
print "look here:" + STATIC_URL

# STATIC_ROOT = os.path.join(BASE_DIR, "static")


STATICFILES_DIRS = (
    os.path.join(SETTINGS_PATH, 'static'),
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
DEFAULT_FROM_EMAIL = 'beckastar@gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False 
EMAIL_PORT = 1025

AUTH_USER_MODEL = 'ladynerds.user'

DATABASES   = {
    'default': {'ENGINE':'django.db.backends.postgresql_psycopg2',
                'NAME': 'ladynerds',
                'USER': 'hacker',
                'PASSWORD' :'python'
    }
}
