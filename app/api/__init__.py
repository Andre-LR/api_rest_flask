from flask import Blueprint, Flask
from flask_restx import Api

from .controller import namespace


def init_api(app: Flask):
	blueprint = Blueprint('Teams', __name__)
	api = Api(blueprint, title='Team API')

	api.add_namespace(namespace)

	app.register_blueprint(blueprint, url_prefix='/teams')
	