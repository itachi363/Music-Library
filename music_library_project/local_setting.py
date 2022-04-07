# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&2*9hyrss#k1z!_r*++_80)oo#dkfm!gj(p5$+)x=inn)dr)8@'

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