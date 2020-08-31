from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'bastian',
        'PASSWORD': 'balthazar',
        'HOST': os.getenv('TEST_DATABASE_SERVICE_HOST'),
        'PORT': os.getenv('TEST_DATABASE_SERVICE_PORT'),
    }
}

NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-package=course_app',
    '--with-xunit',
    '--xunit-file=xunittest.xml',
    '--cover-branches',
    '--cover-html',
    '--exclude-dir-file=exclude_dirs.txt',
    '--exclude-test-file=exclude_tests.txt'
]
