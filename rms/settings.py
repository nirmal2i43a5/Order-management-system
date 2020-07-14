


import os
import django_heroku#to work with database
import  dj_database_url
from decouple import config,Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-u%g0gmxf25m#$o9h5o^z6d1cjir#83u456#)lssqc)==)9*td'

# SECRET_KEY = os.environ.get('SECRET_KEY')

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')#if debug value is true then return True if any other boolean and false then False

DEBUG = False
ALLOWED_HOSTS = ['djangosupermarket.herokuapp.com']


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

# DATABASES = {
#     'default': {
        
        
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         'NAME':'supermarket',
#         'HOST':'djangosupermarket.herokuapp.com',
#         'USER':'',
#         'PASSWORD':'',
        
#     }
# }

DATABASES = {'default':dj_database_url.config(
    
    default='mysql://nirmal:mysql.edu@1999@localhost:3306/supermarket',
    
)}


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
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')#this makes folder images inside static and upload profile_img




#SMTP configuration---django login to email and sent you response



EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')#this is the jjpassword that i use in gmail 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'




#retrieving value from env variables accessing bucket from aws user
AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')#name this django storages modules
print(AWS_ACCESS_KEY_ID)
AWS_SECRETE_ACCESS_KEY=os.environ.get('AWS_SECRETE_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')



AWS_S3_FILE_OVERWRITE = False #if u upload any file then other cannot overwrite ur filename as same name
AWS_DEFAULT_ACL =  None#blc giving its value can cause an issues (future verison of django storage version also may set it to none)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Activate Django-Heroku.
django_heroku.settings(locals())