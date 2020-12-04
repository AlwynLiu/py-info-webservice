from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/user/login/', methods=['post'])
def login():
    """ 登入系统
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
    return '测试login api'


@app.route('/user/loginout/', methods=['post'])
def loginout():
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


@app.route('/user/delete', methods=['delete'])
def deleteUser():
    """ 用户注销
    用户注销账号.
    ---
    tags:
      - 登入登出
    parameters:
      - name: UserInfo
        in: path
        type: string
        required: true
      - name: password
        in: path
        type: string
        required: true
    responses:
      200:
        description: 删除了对象
        schema:
          id: UserInfo
          properties:
            UserName:
              type: string
              default: '千里无风'
            Password:
              type: string
              default: '1234456'
        examples: 注销失败
      404:
        description: 数据找不到了
        examples: 就是数据找不到了

    """
    return '测试loginout api'


@app.route('/order/queryList', methods=['get'])
def getOrderList():
    """ 获取订单列表数据
    获取订单列表数据.
    ---
    tags:
      - 订单处理
    responses:
      200:
        description: 查询所有产生的订单数据
        schema:
          id: OrderInfo
          properties:
            OrderId:
              type: string
              default: '23123213781937829137829'
            OrderName:
              type: string
              default: '魔毯'
            OrderPrice:
                type: string
                default: $ 892301
          examples: {
            "orderId": 123123213213,
            "orderName": '毛毯',
            "orderPrice": "$1321321"
          }
    """
    return {
        "orderId": 123123213213,
        "orderName": '毛毯',
        "orderPrice": "$1321321"
    }


app.run()