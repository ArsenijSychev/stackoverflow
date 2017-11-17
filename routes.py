from views.main import MainView
from views.my_questions import MyQuestionView


routes = {
    '/': MainView.as_view('main'),
    '/oauth/login': MyQuestionView.as_view('my_questions')
}


def setup_routes(app):
    for route, param in routes.items():
        if isinstance(param, list):
            pass
        else:
            app.add_url_rule(route, view_func=param)
