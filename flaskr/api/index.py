#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


from flask import Blueprint, render_template


bp = Blueprint('index', __name__)


@bp.route('/', methods=['get'])
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
    return render_template("./index.html")

