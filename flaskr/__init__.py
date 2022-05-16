from .api import operationDb
from .api import englishCount
from .api import flaskWebApi
from .api import index
from .api import get_os_info

from flask_login import login_manager
from flasgger import Swagger
import os

from flask import Flask, request, url_for, redirect
from .api import auth
app = Flask(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .api import auth
    app.register_blueprint(auth.bp)

    return app


@app.before_request
def is_login():
    pass
    # auth_cookie = request.cookies.get('auth_cookie')
    # if request.path == '/auth/login':
    #     return None
    # if auth_cookie is None:
    #     # return url_for('auth.loginSys')
    #     return redirect(url_for('auth.loginSys', current_url=request.url))

#
# from flask import Flask
# from flasgger import Swagger
#
# from .api import auth
# # from flask_jsonrpc import JSONRPC
#
#
# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )
#
#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)
#
#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass
#
#     from .api import auth
#     app.register_blueprint(auth.bp)
#
#     return app
#


# jsonrpc = JSONRPC(app, '/api', enable_web_browsable_api=True)

# @jsonrpc.method('App.index')
# def index():
#     return 'welcome to Flask JSON-RPC'


app.register_blueprint(auth.bp)
app.register_blueprint(englishCount.bp)
app.register_blueprint(flaskWebApi.bp)
app.register_blueprint(index.bp)

app.register_blueprint(operationDb.bp)
app.register_blueprint(get_os_info.bp)

