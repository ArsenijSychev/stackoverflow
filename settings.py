import os
import ast


def env(key, default=None, is_required=False):
    """
    Get environment from os.environment

    :param key: string -- key of environment
    :param default: string -- default value
    :param is_required: bool -- raise if value is None
    :return: object
    """
    try:
        value = os.environ.get(key, None)

        if not value:
            if is_required:
                raise AttributeError(
                    'Setting `{}` is required in that project.'.format(key))
            return default

        return ast.literal_eval(value)

    except AttributeError as e:
        raise e
    except (SyntaxError, ValueError):
        return value


# Additional config for Flask App
CONFIG = {
}

SECRET_KEY = env('SECRET_KEY', is_required=True)

DEBUG = env('DEBUG', True)

HOST = env('HOST', 'localhost')
PORT = env('PORT', 8000)

TEMPLATES_FOLDER = 'templates'
STATIC_FOLDER = 'static'


STACKOVERFLOW = {
    'QUESTION_URL': 'https://api.stackexchange.com/{api_version}/users/'
                    '{user_id}/questions/?site=stackoverflow&pagesize='
                    '{page_size}&page={page}',
    'PAGE_SIZE': 50,
    'API_VERSION': '2.2',
    'OAUTH_URL': 'https://stackexchange.com/oauth?client_id={client_id}&'
                 'redirect_uri={redirect_uri}',
    'CLIENT_ID': env('STACKOVERFLOW_CLIENT_ID', is_required=True),
    'CLIENT_SECRET': env('STACKOVERFLOW_CLIENT_SECRET', is_required=True),
    'KEY': env('STACKOVERFLOW_KEY', is_required=True),
    'REDIRECT_URI': '{}/oauth/login'.format(
        env('STACKOVERFLOW_DOMAIN_URL', is_required=True).rstrip('/')
    ),
    'ACCESS_TOKEN_URL': 'https://stackexchange.com/oauth/access_token/json',
    'ME_URL': 'https://api.stackexchange.com/{api_version}/me?format=json&'
              'site=stackoverflow&access_token={access_token}&key={key}'
}
