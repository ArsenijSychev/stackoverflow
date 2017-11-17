from flask import render_template, request, session
from flask.views import MethodView

from utils import get_questions_by_user_id, get_oauth_url


class MainView(MethodView):

    def get(self, *args, **kwargs):
        context = {
            'oauth_url': get_oauth_url()
        }

        user_id = session.get('user_id', 0)
        if user_id:
            context['user_id'] = user_id
            context['page'] = 1

            data = get_questions_by_user_id(user_id, 1)
            if data.status_code == 200:
                context['data'] = data.json()
            else:
                context['error'] = {}
                context['error']['common'] = '({}) - {}'.format(
                    data.status_code,
                    data.content
                )

            del session['user_id']

        return render_template('main.html', **context)

    @staticmethod
    def _validate_positive_integer(value):
        if not value:
            return 'This field is required.'
        try:
            value = int(value)
        except (ValueError, TypeError):
            return 'This field must be integer.'

        if value <= 0:
            return 'This field must be more than 0.'

    def post(self, *args, **kwargs):
        user_id = request.values.get('user_id')
        page = request.values.get('page')

        user_id__errors = self._validate_positive_integer(user_id)
        page__errors = self._validate_positive_integer(page)

        context = {
            'user_id': user_id,
            'page': page,
            'oauth_url': get_oauth_url()
        }

        if user_id__errors or \
                page__errors:
            context['error'] = {
                'user_id': user_id__errors,
                'page': page__errors
            }
        else:
            data = get_questions_by_user_id(user_id, page)
            if data.status_code == 200:
                context['data'] = data.json()
            else:
                context['error'] = {}
                context['error']['common'] = '({}) - {}'.format(
                    data.status_code,
                    str(data.content)
                )

        return render_template('main.html', **context)
