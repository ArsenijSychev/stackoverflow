import requests

from flask import render_template, request, session, redirect
from flask.views import MethodView

from settings import STACKOVERFLOW


class MyQuestionView(MethodView):

    def get(self):
        code = request.args.get('code')
        response = requests.post(
            STACKOVERFLOW['ACCESS_TOKEN_URL'],
            json={
                'client_id': STACKOVERFLOW['CLIENT_ID'],
                'client_secret': STACKOVERFLOW['CLIENT_SECRET'],
                'code': code,
                'redirect_uri': STACKOVERFLOW['REDIRECT_URI']
            }
        )

        if response.status_code != 200:
            return render_template('main.html',
                                   error={'common': response.content})

        data = response.json()

        response = requests.get(STACKOVERFLOW['ME_URL'].format(
            access_token=data['access_token'],
            api_version=STACKOVERFLOW['API_VERSION'],
            key=STACKOVERFLOW['KEY']
        ))

        if response.status_code != 200:
            return render_template('main.html',
                                   error={'common': response.content})

        data = response.json()
        session['user_id'] = data['items'][0]['account_id']

        return redirect('/')
