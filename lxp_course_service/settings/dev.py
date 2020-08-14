from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_SERVICE_HOST'),
        'PORT': os.getenv('DATABASE_SERVICE_PORT'),
    }
}

CACHES = {
 "default": {
     "BACKEND": "django_redis.cache.RedisCache",
     "LOCATION": "redis://172.30.238.94:6379/1",
     "OPTIONS": {
         "CLIENT_CLASS": "django_redis.client.DefaultClient",
         "PASSWORD": "somepassword" #TODO: get this from env secret
     }
 }
}
