"""
Django settings for coven project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&b^le+))2=$tnywdp#e$3lev%hv0j284o8%1ch*&1dy%jk=u7&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEV = False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'material.admin',
    'material.admin.default',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'ckeditor',
    'ckeditor_uploader',
    'apps.indicadores',
    'apps.blog',
    'apps.web',
    'fcm_django',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coven.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'coven.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#CONFIGURACION DRF
CORS_ORIGIN_ALLOW_ALL = True  # Permite la api se usada desde cualquier origen
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'MAX_PAGINATE_BY': 100,
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}

if DEV:
    print('Development Environment')
    SITE_URL = 'http://127.0.0.1:8000/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'coven',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }



else:
    SITE_URL = 'https://coven.jaspesoft.com/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db_coven',
            'USER': 'user_admindb',
            'PASSWORD': 'P@ssw0rd2020c0r0n4',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }


MATERIAL_ADMIN_SITE = {
    'HEADER':  'Coven  Admin',  # Admin site header
    'TITLE':  'CoVen',  # Admin site title
    #'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
    #'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
    #'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
    #'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
    #'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
    'LOGIN_LOGO':  'imagen/logo.svg',  # Admin site logo on login page (path to static should be specified)
    #'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
    #'SHOW_THEMES':  True,  #  Show default admin themes button
    #'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
    #'NAVBAR_REVERSE': True,  # Hide side navbar by default
    #'SHOW_COUNTS': True, # Show instances counts for each model
    #'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
    #    'sites': 'send',
    #},
    #'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
    #    'site': 'contact_mail',
    #}
}

# CKEDITOR

CKEDITOR_UPLOAD_PATH = 'post'
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 300,
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            ['RemoveFormat', 'Source']
        ],
        'extraPlugins': ','.join([
            'uploadimage',
            'uploadwidget'
        ]),
    }
}

FCM_DJANGO_SETTINGS = {
        "APP_VERBOSE_NAME": "Push Notifications",
        "FCM_SERVER_KEY": "AAAAHfFw5QE:APA91bHRPFoBVpuCgETCwYxg7av0BV73_M6NXbri8UTIjzdXPSk0H2xVlQcxJkEipAjLbgwR95VuGsnOfJGX7VPiImRlyHLKKcG-G01pRotbiH7nW-bm9xToLOEFKBQcWG2YHKhAByEE",
        "ONE_DEVICE_PER_USER": False,
        "DELETE_INACTIVE_DEVICES": True,
}
