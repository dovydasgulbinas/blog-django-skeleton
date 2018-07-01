from .settings_main import *
# Prod Setting Overrides

print(" {} ".format("using PRODUCTION settings").center(80, '='))

DEBUG = False
SECTION = 'prod'
SECRETS = CONF[SECTION]  # uses section [prod] in secrets.ini

SESSION_COOKIE_SECURE = True
ADMIN_ENABLED = False
SECURE_CONTENT_TYPE_NOSNIFF = True
ALLOWED_HOSTS = ['*']


# JUST AS AN ILLUSTRATIVE EXAMPLE
# overrides sqlite3 DB to a production ready postgress one
# DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
# DATABASES['default']['NAME'] = 'username'
# DATABASES['default']['USER'] = 'password'
# DATABASES['default']['PASSWORD'] = SECRETS['POSTGRESQL_PASSWORD']
# DATABASES['default']['HOST'] = '127.0.0.1'
# DATABASES['default']['PORT'] = '5432'

