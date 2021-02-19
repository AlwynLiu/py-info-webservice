# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""


import os # 文件和目录方法
import datetime
import sys
from flask import Blueprint, render_template


bp = Blueprint("getOsInfo", __name__, url_prefix="/getosinfo")


@bp.route('/')
def index():
    print(sys.platform)
    print(range(100))
    print(sys.version)
    return render_template('systemInfo.html')

