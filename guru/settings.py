"""
Django settings for guru project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*jkfy5vxrim-n@8hvsz=3@!r^kc79-#r#n2-vdod)+m(!u0@_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
 'django.template.loaders.app_directories.Loader')

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    ]

ALLOWED_HOSTS = [
    '.localhost', '127.0.0.1', '.herokuapp.com','.globoi.com'
    ]
# Application definition

INSTALLED_APPS = (
    
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guru.core',
    'guru.home',
    'guru.subscriptions', 
    'embed_video', 

)




MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'guru.urls'

'''

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request', 
    'django.core.context_processors.auth', 
    'django.core.context_processors.debud', 
    'django.core.context_processors.i18n', 



    )
'''


WSGI_APPLICATION = 'guru.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///'+ BASE_DIR.child('db.sqlite3'),
        cast=db_url),

        
    
}


# ESQUEMA DE LOGIN
AUTH_PROFILE_MODULE = 'admin'

LOGIN_URL = 'django.contrib.auth.views.login'

LOGIN_REDIRECT_URL  =  '/'





# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True




EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
    'embed_video.backends.SoundCloudBackend',
    'core.backends.CustomBackend',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'guru/core/static')

MEDIA_URL = '/media/'

STATIC_ROOT = BASE_DIR.child('staticfiles',)

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "core/static"),
    )
print  os.path.join(BASE_DIR, "core/static")
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )