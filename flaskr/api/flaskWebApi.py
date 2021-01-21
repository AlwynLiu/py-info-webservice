# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""

from flask import Blueprint, render_template, request
import string, json


bp = Blueprint('flaskWebApi', __name__, url_prefix='/flaskWebApi')


@bp.route('/user/<name>', methods=['get'])
def user(name):
    """
    访问地址为http://127.0.0.1:5000/flaskWebApi/user/alvin
    :param name:
    :return:
    """
    user_agent = request.headers.get('User-Agent')
    """
    你的浏览器是： Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75
    """
    coments = ['啦啦啦', '哈哈哈', '哦嚯嚯嚯']
    return render_template('./flaskWebApi.html', name=name, coments=coments)
