import functools

from flask import Blueprint, render_template
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
