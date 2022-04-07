# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2k=)$i#jq$w$@q5nb)7fo!y73x9%#7%&gh+)m0fil5!n2&kp64'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}