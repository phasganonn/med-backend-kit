import sqlite3
import os

DB_PATH = "stock.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # 创建药品库存表
    cur.execute('''
    CREATE TABLE IF NOT EXISTS drug_stock (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_name TEXT,
        stock_num INTEGER,
        batch_no TEXT
    )
    ''')
    conn.commit()
    conn.close()

# 初始化库
if not os.path.exists(DB_PATH):
    init_db()

# 数据库操作封装
def db_execute(sql, args=()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    res = cur.execute(sql, args).fetchall()
    conn.commit()
    conn.close()
    return res
