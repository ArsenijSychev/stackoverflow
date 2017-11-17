#!/usr/bin/env python
import settings

from flask import Flask

from routes import setup_routes


app = Flask(
    'Stackoverflow Test',
    template_folder=settings.TEMPLATES_FOLDER,
    static_folder=settings.STATIC_FOLDER
)

app.debug = settings.DEBUG
app.secret_key = settings.SECRET_KEY
# Update default settings
app.config.update(settings.CONFIG)
# Setup routes
setup_routes(app)


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT
    )
