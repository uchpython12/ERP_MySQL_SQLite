ERP 分為 連線版 和 單機版

連線版 ERP介面+MYSQL資料庫

單機版ERP介面+SQLite資料庫

單機版 直接執行 ERP系統單機版_sqlite.py 即可運行

連線版需要先 連接MySQL 才可以運行

host = 'localhost'


user = 'admin'


passwd = 'admin'


db = "mydatabase"


tableName="erptable"


建立 db = "mydatabase"

導入erptable.sql

