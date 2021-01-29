#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"


from flask import Blueprint, render_template


bp = Blueprint('index', __name__)


@bp.route('/', methods=['get'])
def index():
    """
    显示首页数据
    ---
    tags:
        - 首页
    """
    return render_template("./index.html")

