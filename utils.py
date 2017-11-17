import requests

from settings import STACKOVERFLOW


def get_questions_by_user_id(user_id, page=1):
    response = requests.get(
        url=STACKOVERFLOW['QUESTION_URL'].format(
            user_id=user_id,
            page_size=STACKOVERFLOW['PAGE_SIZE'],
            page=page,
            api_version=STACKOVERFLOW['API_VERSION']
        )
    )

    return response


def get_oauth_url():
    return STACKOVERFLOW['OAUTH_URL'].format(
        client_id=STACKOVERFLOW['CLIENT_ID'],
        redirect_uri=STACKOVERFLOW['REDIRECT_URI']
    )
