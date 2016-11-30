
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = '@+34_9x66^ww_fw)w&*i_(&a$f#n0kfrsfw^(j($m&*aw=4-6w'

ALLOWED_HOSTS = [u'jamatapp.herokuapp.com',
                u'localhost',
                u'adils.me'
]

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'restapi.apps.RestapiConfig',
    #'rest_framework.authtoken',
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

ROOT_URLCONF = 'jamatoclock.urls'

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

WSGI_APPLICATION = 'jamatoclock.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#database
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1un1f26uqq29k',
        'USER': 'sogotdcylyzhah',
        'PASSWORD': 'rDwefrY2Z4_0eKOPLCDh-hfSbG',
        'HOST': 'ec2-54-243-202-174.compute-1.amazonaws.com',
        'PORT': '5432',
        'sslmode':'require'
    },


}'''

#DATABASE_URL=$(heroku config:get DATABASE_URL -a your-app) your_process

import dj_database_url

DATABASES = {}
DATABASES['default'] = dj_database_url.config(default = 'postgres://sogotdcylyzhah:rDwefrY2Z4_0eKOPLCDh-hfSbG@ec2-54-243-202-174.compute-1.amazonaws.com:5432/d1un1f26uqq29k')

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}
# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')