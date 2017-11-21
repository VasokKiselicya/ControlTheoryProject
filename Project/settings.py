"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '4_y*@hf!ja2*wonf-66ivh05vo=b(76(^#ktqb_6=qb9x_rjr8'

DEBUG = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['controltheory.herokuapp.com', 'vincent-project.herokuapp.com', '127.0.0.1']

RAVEN_CONFIG = {
    'dsn': 'https://0f1ad400c39c44b7bdce0c7ceb25e608:aac13a9ba9a543aeb1a39074f57ce59f@sentry.io/217895',
}

INSTALLED_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    "django.contrib.sites",
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # 'raven.contrib.django.raven_compat',
    "ckeditor",
    # "account",
    'rosetta',
    "db",
    "core"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'
APPEND_SLASH = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# Locale Settings
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian'))
)

ROSETTA_MESSAGES_PER_PAGE = 25
ROSETTA_SHOW_AT_ADMIN_PANEL = True

ugettext = lambda x: x


WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'davo3thk0t6eg8',
        'USER': 'zlgpeqpeipmydl',
        'PASSWORD': 'bc3f5e3a5d20e6ce21218fb60f6bb5bc609bae6df8e85f4d5d78a1494349fbd9',
        'HOST': 'ec2-46-137-97-169.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
        "SSL": "OFF"
    }
}


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S",
            'fmt': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logs/logfile.txt",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

UPLOAD_PATH = os.path.join(PROJECT_ROOT, 'static') if DEBUG else STATIC_ROOT

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# MEDIA_URL = '/media/'
#
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# AUTH SETTINGS
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = True
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

# SOCIAL AUTH SETTINGS


# MAIL SETTINGS

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'VincentTheory'
EMAIL_HOST_USER = 'vincent.study.company@gmail.com'
EMAIL_PORT = 587
FROM_EMAIL = 'Vincent Company <vincent.study.company@gmail.com>'
DEFAULT_FROM_EMAIL = FROM_EMAIL

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'office2013',
        'toolbar': 'Custom',
        'height': 400,
        'width': 800,
        'removePlugins': 'stylesheetparser',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Custom': [
            {"name": 'document',
             "items": ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {"name": 'clipboard',
             "items": ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {"name": 'editing', "items": ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
            {"name": 'forms',
             "items": ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button',
                       'ImageButton', 'HiddenField']},
            '/',
            {"name": 'basicstyles',
             "items": ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
                       'RemoveFormat']},
            {"name": 'paragraph',
             "items": ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
                       'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                       'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
            {"name": 'links', "items": ['Link', 'Unlink', 'Anchor']},
            {"name": 'insert',
             "items": ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar',
                       'PageBreak', 'Iframe']},
            '/',
            {"name": 'styles', "items": ['Styles', 'Format', 'Font', 'FontSize']},
            {"name": 'colors', "items": ['TextColor', 'BGColor']},
            {"name": 'tools', "items": ['Maximize', 'ShowBlocks']},
            {"name": 'about', "items": ['About']}
        ],
        'tabSpaces': 4
    }
}
