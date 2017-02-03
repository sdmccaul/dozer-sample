#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.config.from_pyfile('config/api.cfg')

os.environ['QUERY_URL'] = app.config['QUERY_URL']
os.environ['UPDATE_URL'] = app.config['UPDATE_URL']
os.environ['UPDATE_EMAIL'] = app.config['UPDATE_EMAIL']
os.environ['UPDATE_PASS'] = app.config['UPDATE_PASS']

from routes.fisfeed import fisfeed
from routes.citations import citations
from routes.harvest import harvest

app.register_blueprint(fisfeed)
app.register_blueprint(citations)
app.register_blueprint(harvest)

from resources.errors import ValidationError, AliasError, RESTError

@app.errorhandler(RESTError)
def handle_rest_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
	app.run(host='0.0.0.0')