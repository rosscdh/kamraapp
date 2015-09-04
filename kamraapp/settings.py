# -*- coding: utf-8 -*-
"""
Django settings for kamraapp project.

Generated by 'django-admin startproject' using Django 1.8.4.

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
SECRET_KEY = '9!ceu3zg_jrqqkccn+ilfd!t^kfjsk-hg#!a+ii^ue-oi$+gd8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

APPLICATION_APPS = (
    'kamraapp.apps.bet',
)

HELPER_APPS = (
    'pipeline',
    'formtools',
    'corsheaders',
    'djangobower',
    'crispy_forms',
    'pinax.eventlog',
    'django_extensions',
    'rest_framework',
)


INSTALLED_APPS = DJANGO_APPS + HELPER_APPS + APPLICATION_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

ROOT_URLCONF = 'kamraapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kamraapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

BOWER_COMPONENTS_ROOT = BASE_DIR

STATICFILES_DIRS = (
    BOWER_COMPONENTS_ROOT + '/bower_components',
)

BOWER_INSTALLED_APPS = (
    'angularjs',
    'angular-resource',
    'angular-sanitize',
    'angular-ui-router',
    'angular-moment',
    'moment',
    'angular-loading-bar',
    'angular-smart-table',
)

PIPELINE_JS = {
    'dashboard': {
        'source_filenames': (
            # support
            'jquery/dist/jquery.js',
            'bootstrap/dist/js/bootstrap.js',
            # angular
            'angular/angular.js',
            'angular-ui-router/release/angular-ui-router.js',
            'angular-resource/angular-resource.js',
            'angular-sanitize/angular-sanitize.js',
            # moment timestamps
            'moment/moment.js',
            'angular-moment/angular-moment.js',
            # loading bar
            'angular-loading-bar/build/loading-bar.js',
            # table
            'angular-smart-table/dist/smart-table.js',
            # main app
            'js/project-list-app.js',
        ),
        'output_filename': 'js/dashboard.js',
    },
}

PIPELINE_CSS = {
    'dashboard': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.css',
            # loading bar
            'angular-loading-bar/build/loading-bar.css',
        ),
        'output_filename': 'css/dashboard.css',
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.sass.SASSCompiler',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework.filters.DjangoFilterBackend',
    # ),
    'PAGINATE_BY': 5
}

REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 2
}

try:
    from .local_settings import *
except:
    pass
