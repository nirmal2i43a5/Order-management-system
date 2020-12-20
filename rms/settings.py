


import os
import django_on_heroku#to work with database
import  dj_database_url
from decouple import config,Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!



SECRET_KEY = config("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')#if debug value is true then return True if any other boolean and false then False

DEBUG = True


ALLOWED_HOSTS = ['djangosupermarket.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #later install
    'import_export',
    
    'widget_tweaks',
    'crispy_forms',
    'django_filters',
    'bootstrap_modal_forms',
    
    'customers',
    'products',
    'orders',
    'registers',
    'django.contrib.humanize',
    #for deploy
    'storages',
     
    
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

ROOT_URLCONF = 'rms.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'rms.wsgi.application'

# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

"""
Using below database is for development and postgres is for production (for postgres u dont need to verify in settings .py)

"""


# DATABASES = {
#     'default': {
        
        
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'NAME':'supermarket',
#         'HOST':'127.0.0.1',
#         'USER':config('db_user'),
#         'PASSWORD':config('db_password')
        
#     }
# }


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True



CRISPY_TEMPLATE_PACK = 'bootstrap4'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


LOGOUT_REDIRECT_URL = '/user/login'

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')#heroku hold in this way for satic files

STATICFILES_DIRS =[os.path.join(BASE_DIR,"static")]




#for image upload
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')#this makes folder media and hold images Profile_images inside static and upload profile_img



#SMTP configuration---django login to email and sent you response



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_USER = 'nirmalpandey27450112@gmail.com'
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')#this is the jjpassword that i use in gmail 
EMAIL_HOST_PASSWORD = 'ffutdfvwvodrjztp'#I USE app password from gmail  BECAUSE OF ERROR DURING FORGET PASSWORD and it is more secure
# print(EMAIL_HOST_USER)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

"""Mainly i use aws s3 for storing images but due to my aws account suspension i remove below code and store image in default system .But using below send image to aws if my account works

# #retrieving value from env variables accessing bucket from aws user
AWS_ACCESS_KEY_ID=config('AWS_ACCESS_KEY_ID')#name this django storages modules
AWS_SECRET_ACCESS_KEY=config('AWS_SECRETE_ACCESS_KEY')
#when using heroku we use AWS_SECRETE_ACCESS_KEY but in normal(i.e for aws) AWS_SECRET_ACCESS_KEY  i.e SECRET vs SECRETE (Using SECRET I GET ERROR)

AWS_STORAGE_BUCKET_NAME=config('AWS_STORAGE_BUCKET_NAME')


AWS_S3_FILE_OVERWRITE = False #(from django storages)if u upload any file then other cannot overwrite ur filename as same name
AWS_DEFAULT_ACL =  None#blc giving its value can cause an issues (future verison of django storage version also may set it to none)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_REGION_NAME = 'ap-south-1' 

"""

# Activate Django-Heroku.
#it configures database ,allowed hosts and many other that suits heroku env setting
django_on_heroku.settings(locals())
