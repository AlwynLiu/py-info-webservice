from flask import Blueprint, render_template, request
import string, json


bp = Blueprint('operationdb', __name__, url_prefix='/operationdb')


@bp.route('/index', methods=['get'])
def update():
    """ 更新数据
    批量更新数据库数据，从其他表的数据中更新
    ---
    tags:
      - 数据库操作
    parameters:
      - sql:
        type: string
        default: all
    responses:
      200:
        description: success
        examples:
          data: success
    """
    return render_template("./operationdb/index.html")

