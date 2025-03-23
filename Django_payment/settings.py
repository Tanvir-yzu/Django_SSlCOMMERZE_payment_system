import os

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i*gvyhhwges&ux*u3uu+2yr$q2euv^y0yjxkd4j#&uv#065ym_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_payment.urls'

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

WSGI_APPLICATION = 'Django_payment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SSLCOMMERZ Settings
SSLCOMMERZ_SETTINGS = {
    'store_id': os.getenv('SSLC_STORE_ID'),
    'store_pass': os.getenv('SSLC_STORE_PASSWORD'),
    'issandbox': os.getenv('SSLC_SANDBOX', 'True') == 'True'
}


# CSRF Settings
# CSRF_TRUSTED_ORIGINS = [
#     'http://127.0.0.1:8000',
#     'http://*.localhost:8000',
#     'http://localhost:8000',
#     'http://127.0.0.1',
#     'http://localhost',
#     'https://127.0.0.1:8000', # Add this to handle requests with null origin
#     'https://sandbox.sslcommerz.com',
# ]

# CSRF_COOKIE_SECURE = False  # Set to True in production with HTTPS
# CSRF_COOKIE_HTTPONLY = False  # Allows JavaScript to access the CSRF token
# CSRF_USE_SESSIONS = True  # Store CSRF token in the session instead of a cookie

# Session Settings
# SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
# SESSION_COOKIE_HTTPONLY = True  # Prevents JavaScript from accessing the session cookie

# Add this setting to exempt specific views from CSRF protection
# CSRF_EXEMPT_URLS = [
#     r'^payment/success/$',
#     r'^payment/fail/$',
#     r'^payment/cancel/$',
# ]
# Security Settings (for production)
# if not DEBUG:
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_SSL_REDIRECT = True
#     X_FRAME_OPTIONS = 'DENY'