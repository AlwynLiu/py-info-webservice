import functools

from flask import Blueprint, render_template, request, make_response, redirect
from flasgger import Swagger

# app = Flask(__name__)
# swagger = Swagger(app)


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['get'])
def loginSys():
    """ 用户登录
    用户登录到系统
    ---
    tags:
      - 登入登出
    parameters:
      - userName:
        type: string
        required: true
        default: all
      - password:
        type: string
        required: true
        default: all
    responses:
      200:
        description: success
        examples:
          data: success
    """
    return render_template('./auth/login.html')


@bp.route('/account', methods=['get', 'post'])
def account_login():
    request.args.get('username')
    request.args.get('password')
    response = make_response(redirect('/'))
    response.set_cookie("auth_cookie", "login", max_age=3600)
    return response
