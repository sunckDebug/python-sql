from flask import Flask
from MySqlConn import *
from datetime import datetime, date
from decimal import Decimal
import pymysql, json



# 解决日期时间 Decimal 等类型不能josn的问题
class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, Decimal):
            return float(o)
        else:
            return json.JSONEncoder.default(self, o)


app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    sql = """select * from six_in_one_che"""
    data = dictQuery(sql)
    return json.dumps({"code": 1, "message": data}, cls=DateEncoder, ensure_ascii=False)


@app.route("/add", methods=["GET"])
def add():
    sql = """INSERT INTO xincai_stats(qrcode, onlycode, payCode, busyCode)
                               VALUES('http://www.baidu.com', '000001',  '410321597974561s', 'jk-45454545446')"""

    try:
        insert_delete_update(sql)
        return json.dumps({"code": 1, "message": "添加成功"}, cls=DateEncoder, ensure_ascii=False)
    except pymysql.err.IntegrityError as err:
        rollback()
        return json.dumps({"code": 0, "message": "操作失败关键字重复"}, cls=DateEncoder, ensure_ascii=False)



@app.route("/del", methods=["GET"])
def delete():
    sql = """DELETE FROM batch where openrate="%s" """ % "凯旋路支行123"

    try:
        insert_delete_update(sql)
        return json.dumps({"code": 1, "message": "删除成功"}, cls=DateEncoder, ensure_ascii=False)
    except Exception as err:
        rollback()
        return json.dumps({"code": 0, "message": "操作失败关键字重复"}, cls=DateEncoder, ensure_ascii=False)


@app.route("/upd", methods=["GET"])
def update():
    sql = """update batch set openrate = "%s" where id = %d""" % ('凯旋路支行123', 12)

    try:
        insert_delete_update(sql)
        return json.dumps({"code": 1, "message": "修改成功"}, cls=DateEncoder, ensure_ascii=False)
    except Exception as err:
        rollback()
        return json.dumps({"code": 0, "message": "操作失败关键字重复"}, cls=DateEncoder, ensure_ascii=False)



if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=8080,
        debug=True
    )