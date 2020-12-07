import functools

from flask import Blueprint
from flasgger import Swagger

# app = Flask(__name__)
# swagger = Swagger(app)


bp = Blueprint('auth', __name__)


@bp.route('/delete', methods=['get'])
def deleteUser():
    """ 登出系统
    登录到系统获取颜色.
    ---
    tags:
      - 登入登出
    parameters:
      - name: palette
        in: path
        type: string
        enum: ['全部', 'rgb', 'cmyk']
        required: true
        default: all
    responses:
      200:
        description: 颜色的列表(数据对象)
        examples:
          rgb: ['red', 'green', 'blue']
    """
    return '测试loginout api'


