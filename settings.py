# -*- coding: utf-8 -*-
"""
@Author ： Alvin.Liu
"""


class BaseConfig(object):
    ENV = None                                  # 虚拟环境，当前项目运行环境
    DEBUG = True                                # 是否开启debug模式
    SECRET_KEY = "secret_key"                   # session秘钥配置
    TESTING = False
    DATABASE_URI = 'sqlite://:memory'
    JSONIFY_MIMETYPE = "application/json"       # 设置jsonify响应时返回的contentype类型


class ProductionConfig(BaseConfig):
    # DATABASE_URI = 'production'
    pass


class DevelopmentConfig(BaseConfig):
    # DATABASE_URI = 'Development'
    pass


class TestingConfig(BaseConfig):
    # DATABASE_URI = 'Testing'
    pass

