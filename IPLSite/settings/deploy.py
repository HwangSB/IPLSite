from .base import *
import json

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

WSGI_APPLICATION = 'IPLSite.wsgi.application'

DEBUG = False

ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']