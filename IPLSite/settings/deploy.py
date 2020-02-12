from .base import *
import os
import json

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'IPLSite.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

DEBUG = False
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']