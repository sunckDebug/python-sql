import pymysql


# 打开数据库连接
conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="aggregate_pay",
    charset="utf8mb4"
)


# 获取连接下的游标
cursor = conn.cursor()


# 查询类操作获取元组
def tupleQuery(sql):
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        return data
    except Exception as err:
        print(err)
        return err


# 查询类操作获取字典
def dictQuery(sql):
    try:
        cursor.execute(sql)
        desc = cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        data = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]  # 列表表达式把数据组装起来
        return data
    except Exception as err:
        print(err)
        return err


# 插入删除更新类操作 不捕获报错
def insert_delete_update(sql):
    cursor.execute(sql)
    conn.commit()


# 提交数据操作
def commit(): conn.commit()


# 回滚操作
def rollback(): conn.rollback()


# 关闭数据库连接
def close(): conn.close()