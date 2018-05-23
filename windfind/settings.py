"""
Django settings for windfind project.

Generated by 'django-admin startproject' using Django 1.8.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1tkal3@c60)_9$omcky^i6+b0w_l8$z21*%w7porm&bl82tq3q'

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
    'ruckus_ipudong1',
    'h3c_ishanghai',
    'h3c_ipudong3',
    'account',
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

ROOT_URLCONF = 'windfind.urls'

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

WSGI_APPLICATION = 'windfind.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'test',
        'PASSWORD': 'qwe123,.',
        'HOST': '10.0.2.74',
        'PORT': '3306',
    },
    'ruckus_ipudong1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ruckus_ipudong1',
        'USER': 'test',
        'PASSWORD': 'qwe123,.',
        'HOST': '10.0.2.74',
        'PORT': '3306',
    },
    'h3c_ishanghai': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'h3c_ishanghai',
        'USER': 'test',
        'PASSWORD': 'qwe123,.',
        'HOST': '10.0.2.74',
        'PORT': '3306',
    },
    'h3c_ipudong3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'h3c_ipudong3',
        'USER': 'test',
        'PASSWORD': 'qwe123,.',
        'HOST': '10.0.2.74',
        'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['windfind.database_router.DatabaseAppsRouter']
DATABASE_APPS_MAPPING = {
    # example:
    #'app_name':'database_name',
    'ruckus_ipudong1': 'ruckus_ipudong1',
    'h3c_ishanghai': 'h3c_ishanghai',
    'h3c_ipudong3':'h3c_ipudong3',
}

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
