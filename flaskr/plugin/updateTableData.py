import pymysql

connection = pymysql.connect("127.0.0.1", "alvin2", "123456", "podata")

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = """SELECT b.`emp_family_name`, b.`emp_first_name`, b.`email_suffix`, b.`emp_position`, b.`birthday`, b.`hire_date`, b.`domainacc`, b.`emp_fire_date`, b.`phfloc`, b.`phflocdescr`, b.`socloc`, b.`soclocdescr`,b.`prc_dt`,b.`exp_prc_dt_end`,b.`workcitycode`,b.`bu`,b.`budescr`, b.`contractloc`, b.`contractlocdescr`, b.`eid`
FROM hris_employee AS a LEFT JOIN hris_employee_20201222 AS b
ON a.`eid` = b.`eid`"""
        cursor.execute(sql)
        result = cursor.fetchall()
        updatesql = "update hris_employee set emp_family_name=(%s), emp_first_name=(%s), email_suffix=(%s), emp_position=(%s), birthday=(%s), hire_date=(%s), domainacc=(%s), emp_fire_date=(%s), phfloc=(%s), phflocdescr=(%s), socloc=(%s), soclocdescr=(%s), prc_dt=(%s), exp_prc_dt_end=(%s), workcitycode=(%s), bu=(%s), budescr=(%s), contractloc=(%s), contractlocdescr=(%s) where eid=(%s)"
        cursor.executemany(updatesql, result)
        print('执行完成')
finally:
    connection.close()
