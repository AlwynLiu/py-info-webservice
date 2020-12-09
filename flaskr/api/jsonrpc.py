from flask import Blueprint, render_template
from flasgger import Swagger

# app = Flask(__name__)
# swagger = Swagger(app)


rbp = Blueprint('auth', __name__, url_prefix='/auth')

from flask_jsonrpc import JSONRPC

# app = Flask(__name__)
jsonrpc = JSONRPC(rbp, '/api', enable_web_browsable_api=True)

