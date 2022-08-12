'''
Config : UTF-8

Title : sqlite3 생성/입력/검색 프로세스 함수 스크립트 v1

Write : 22.05.17 / Update :22.05.17

'''
import sqlite3

# 스키마 생성
#s_name = "board.db"
#conn = sqlite3.connect(s_name)
#conn.execute('CREATE TABLE board(id INTEGER, name TEXT, data_01 TEXT, data_02 TEXT)')
#conn.commit()
#conn.close()

#
def show_all():
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM board")
    #
    items = c.fetchall()
    for item in items: print(item)
    #
    conn.commit()
    conn.close()
#
def add_one(id,name,data_01,data_02):
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    c.execute("INSERT INTO board VALUES (?,?,?,?)",(id,name,data_01,data_02))
    #
    conn.commit()
    conn.close()
#
def add_many(list):
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    c.executemany("INSERT INTO board VALUES (?,?,?,?)",(list))
    #
    conn.commit()
    conn.close()
#
def del_one(rowid):
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    c.execute("DELETE FROM board WHERE rowid = (?)",(rowid))
    #
    conn.commit()
    conn.close()
#
def search_data(data):
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM board WHERE data_02 = (?)",(data,))
    #
    items = c.fetchall()
    for item in items: print(item)
    #
    conn.commit()
    conn.close()
#
def update():
    conn = sqlite3.connect("board.db")
    c = conn.cursor()
    #
    conn.commit()
    conn.close()
#
## secu_board
#
#
def show_all_1():
    conn = sqlite3.connect("secu_board.db")
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM board")
    #
    items = c.fetchall()
    for item in items: print(item)
    #
    conn.commit()
    conn.close()
#
def add_one_1(date,title,part):
    conn = sqlite3.connect("secu_board.db")
    c = conn.cursor()
    c.execute("INSERT INTO board VALUES (?,?,?)",(date,title,part))
    #
    conn.commit()
    conn.close()
#
def add_many_1(list):
    conn = sqlite3.connect("secu_board.db")
    c = conn.cursor()
    c.executemany("INSERT INTO board VALUES (?,?,?)",(list))
    #
    conn.commit()
    conn.close()
