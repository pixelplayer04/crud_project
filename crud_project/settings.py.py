DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crud_db',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'student_list'

LOGOUT_REDIRECT_URL = 'login'