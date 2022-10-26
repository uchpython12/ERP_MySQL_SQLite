import pymysql as MySQLdb

host = 'localhost'
user = 'admin'
passwd = 'admin'
db = "mydatabase"
tableName="erptable"

#本機
db = MySQLdb.connect(host=host,  # 連接到本身的電腦IP
                     user=user,  # MySQL/PHPMyAdmin 新增的 用戶
                     passwd=passwd,
                     db=db)  # MySQL/PHPMyAdmin 新增的 資料庫
cursor = db.cursor()

def erpsql_SELECT():
    sql="SELECT * FROM `"+tableName+"` WHERE 1"
    cursor.execute(sql)
    list1= cursor.fetchall()
    db.commit()
    return list1

def erpsql_INSERT(list2):

    sql = "INSERT INTO "+tableName+" (`id`, `品項`, `品牌`, `產品價格`, " \
          "`進貨量`, `儲藏條件`, `所在地`, `進貨人員`, `進貨日期`)" \
          " VALUES (null, %s, %s ,%s ,%s,%s,%s ,%s,%s)"
    val = (list2[0], list2[1],str(list2[2]) ,str(list2[3]),list2[4],list2[5],list2[6],list2[7])
    cursor.execute(sql, val)
    db.commit()

def erpsql_UPDATE(list2,id):

    sql="UPDATE `"+tableName+"` SET `品項`=%s,`品牌`=%s," \
        "`產品價格`=%s,`進貨量`=%s,`儲藏條件`=%s," \
        "`所在地`=%s,`進貨人員`=%s,`進貨日期`=%s WHERE id=%s"
    print(list2)
    val = (list2[0], list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],id)
    cursor.execute(sql,val)
    db.commit()

def erpsql_DELETE(id):
    sql="DELETE FROM `"+tableName+"` WHERE id =%s"
    cursor.execute(sql,id)
    db.commit()
