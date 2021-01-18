import pymysql

connection = pymysql.connect(host = 'localhost', #host属性
                             user = 'alvin1', #用户名
                             password = 'liu1304890',  #此处填登录数据库的密码
                             db = 'novel' #数据库名
                             )


try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     # sql = "INSERT INTO `id` `author` VALUES (2, 'alvin')"
    #     sql = "INSERT INTO `novel_info` (`author`) VALUES (%s)"
    #     cursor.execute(sql, ('千里无风'))
    #     # cursor.execute(sql)
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `author` FROM `novel_info`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
except:
    raise
finally:
    connection.close()