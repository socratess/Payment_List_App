"""
Django settings for payment_list project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from . import applications_social_settings
import os
#from django.utils.timezone import timedelta
from datetime import timedelta
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# _____________________________New variable_____________________________
#Used for a default title or generic 
APP_NAME = 'Payment-Bill'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#^l$!8o9)t8%b7wec4zledf4vu#-&!5n7gcg1472zqu=f%yyqh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bills.apps.BillsConfig',
    'home.apps.HomeConfig',
    'about.apps.AboutConfig',
    'authentication.apps.AuthenticationConfig',
    'account_settings.apps.AccountSettingsConfig',
    'social_django',
    'crispy_forms',
    'crispy_bootstrap4',
    'import_export',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django_auto_logout.middleware.auto_logout',
]

ROOT_URLCONF = 'payment_list.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        # 'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.settings', 
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

WSGI_APPLICATION = 'payment_list.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'Payment_List', 
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'



# Email settings details

env = environ.Env()
environ.Env.read_env()





EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # Name for all the SenGrid accounts
EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')
#EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY')

# The email you'll be sending emails from
DEFAULT_FROM_EMAIL = env('FROM_EMAIL', default='noreply@gmail.com')
#LOGIN_REDIRECT_URL = 'success'

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
]






#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES':(
#        'rest_framework.authentication.BasicAuthentication',
#        'rest_framework.authentication.SessionAuthentication',
#    )
#}

# Configuration the social login

try:
    SOCIAL_AUTH_GITHUB_KEY = applications_social_settings.SOCIAL_AUTH_GITHUB_KEY
    SOCIAL_AUTH_GITHUB_SECRET = applications_social_settings.SOCIAL_AUTH_GITHUB_SECRET
    
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = applications_social_settings.SOCIAL_AUTH_GOOGLE_KEY
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = applications_social_settings.SOCIAL_AUTH_GOOGLE_SECRET
    
except:
    print('When you want to use social login, please see the settings')



AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
    #'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    #'social_core.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

SESSION_EXPIRE_AT_BROWSER_CLOSE= True
AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=5),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'MESSAGE': 'The session has expired for inactivity. Please login again to continue.',
}
