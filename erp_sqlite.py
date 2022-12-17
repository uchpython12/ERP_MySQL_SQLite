import sqlite3 as MySQLdb

db = MySQLdb.connect('mydatabase.db')
cursor = db.cursor()
tableName = "erptable"
#創建表
def erpsql_CREATE_TABLE():
    sql ="""
    CREATE TABLE `erptable` (
  `id` INTEGER PRIMARY KEY,
  `品項` varchar(255) DEFAULT NULL,
  `品牌` varchar(255) DEFAULT NULL,
  `產品價格` varchar(255) DEFAULT NULL,
  `進貨量` int(11) DEFAULT NULL,
  `儲藏條件` varchar(255) DEFAULT NULL,
  `所在地` varchar(255) DEFAULT NULL,
  `進貨人員` varchar(255) DEFAULT NULL,
  `進貨日期` date DEFAULT NULL
  )
    """
    cursor.execute(sql)
#新增資料
def erpsql_INSERT(list2):
    sql = "INSERT INTO " + tableName + " (`id`, `品項`, `品牌`, `產品價格`, " \
    "`進貨量`, `儲藏條件`, `所在地`, `進貨人員`, `進貨日期`)" \
    " VALUES (null,?,?,?,?,?,?,?,?)"
    val = (list2[0], list2[1], list2[2], list2[3], list2[4], list2[5], list2[6], list2[7])
    cursor.execute(sql,val)  # 執行新增資料
    db.commit()  # 送出
# 查詢
def erpsql_SELECT():
    sql="SELECT * FROM `"+tableName+"` WHERE 1"
    cursor.execute(sql)
    list1= cursor.fetchall()
    db.commit()
    return list1
def 顯示資料():
    for row in erpsql_SELECT():
        str1 = ""
        for col in row:
            str1 = str1 +str(col) + ","
        print("筆", str1)
def erpsql_UPDATE(list2,id):

    sql="UPDATE `"+tableName+"` SET `品項`=?,`品牌`=?," \
        "`產品價格`=?,`進貨量`=?,`儲藏條件`=?," \
        "`所在地`=?,`進貨人員`=?,`進貨日期`=? WHERE id=?"
    print(list2)
    val = (list2[0], list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],id)
    cursor.execute(sql,val)
    db.commit()
def erpsql_DELETE(id):
    sql="DELETE FROM `"+tableName+"` WHERE id =?"
    cursor.execute(sql,str(id))
    db.commit()


try:
    #創建資料表
    erpsql_CREATE_TABLE()
except:
    print("mydatabase 已經存在")
    # #新增資料
    # list1=["0", "1", "2", "3", "4", "5", "6", "7"]
    # erpsql_INSERT(list1)
    # # 刪除
    # erpsql_DELETE(3)
    # #更新資料
    # 更新資料=["更新", "1", "2", "3", "4", "5", "6", "7"]
    # erpsql_UPDATE(更新資料,1)
    # #顯示資料
    # 顯示資料()



