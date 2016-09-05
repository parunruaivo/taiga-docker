from .common import *

def convert_boolean(value):
    return True if value.lower() == 'true' else False

DEBUG = convert_boolean('{{DEBUG}}')
TEMPLATE_DEBUG = convert_boolean('{{TEMPLATE_DEBUG}}')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{DB_NAME}}',
        'HOST': '{{DB_HOST}}',
        'PORT': {{DB_PORT}},
        'USER': '{{DB_USER}}',
        'PASSWORD': '{{DB_PASS}}'

    }
}

ADMINS = (
    ('{{TAIGA_ROOT_USERNAME}}','{{TAIGA_ROOT_EMAIL}}'),
)

MEDIA_ROOT = '{{TAIGA_HOME}}/taiga-back/media'
STATIC_ROOT = '{{TAIGA_HOME}}/taiga-back/static'

SITES['api']['domain'] = '{{TAIGA_HOST}}'
SITES['front']['domain'] = '{{TAIGA_HOST}}'

SCHEME = 'https' if convert_boolean('{{TAIGA_HTTPS}}') else 'http'

MEDIA_URL = SCHEME + '://{{TAIGA_HOST}}/media/'
STATIC_URL = SCHEME + '://{{TAIGA_HOST}}/static/'
ADMIN_MEDIA_PREFIX = SCHEME + '://{{TAIGA_HOST}}/static/admin/'

SITES['api']['scheme'] = SCHEME
SITES['front']['scheme'] = SCHEME

SECRET_KEY = '{{TAIGA_SECRET_KEY}}'

DEFAULT_FROM_EMAIL = '{{DEFAULT_FROM_EMAIL}}'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

PUBLIC_REGISTER_ENABLED = convert_boolean('{{PUBLIC_REGISTER_ENABLED}}')
STATS_ENABLED = convert_boolean('{{STATS_ENABLED}}')
WEBHOOKS_ENABLED = convert_boolean('{{WEBHOOKS_ENABLED}}')
FRONT_SITEMAP_ENABLED = convert_boolean('{{FRONT_SITEMAP_ENABLED}}')

INSTALLED_APPS += ['taiga_contrib_slack']

if convert_boolean('{{GITHUB_ENABLED}}'):
    GITHUB_URL = '{{GITHUB_URL}}'
    GITHUB_API_URL = '{{GITHUB_API_URL}}'
    GITHUB_API_CLIENT_ID = '{{GITHUB_API_CLIENT_ID}}'
    GITHUB_API_CLIENT_SECRET = '{{GITHUB_API_CLIENT_SECRET}}'

if convert_boolean('{{EMAIL_ENABLED}}'):
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_USE_TLS = convert_boolean('{{EMAIL_USE_TLS}}')
    EMAIL_HOST = '{{EMAIL_HOST}}'
    EMAIL_HOST_USER = '{{EMAIL_USER}}'
    EMAIL_HOST_PASSWORD = '{{EMAIL_PASS}}'
    EMAIL_PORT = {{EMAIL_PORT}}

if convert_boolean('{{CELERY_ENABLED}}'):

    from .celery import *

    CELERY_ENABLED = True
    AMQP_URL = "amqp://{{AMQP_USER}}:{{AMQP_PASS}}@{{AMQP_HOST}}:{{AMQP_PORT}}"

    BROKER_URL = AMQP_URL + '/{{CELERY_AMQP_NAME}}'
    CELERY_RESULT_BACKEND = 'redis://{{REDIS_HOST}}:{{REDIS_PORT}}/{{REDIS_DB_NUMBER}}'

    if convert_boolean('{{EVENTS_ENABLED}}'):
        EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
        EVENTS_PUSH_BACKEND_OPTIONS = {"url": AMQP_URL + "/{{EVENTS_AMQP_NAME}}"}
