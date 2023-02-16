import sqlite3
from datetime import date


def create_table(names = ["keegan","rahil"],database = "attendance.db" ,table ="attendance"):
    HELLO = "CREATE TABLE {}(name VARCHAR(25) PRIMARY KEY )".format(table)
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(HELLO)
    for i in names:
        QUERY = "INSERT INTO attendance VALUES(\"{}\")".format(i)
        cur.execute(QUERY)
    con.commit()

    QUERY = "SELECT name FROM attendance ORDER BY name" 
    for row in cur.execute(QUERY):
        print(row)

def adding_date(table = "attendance", database = "attendance.db"):
    today = str(date.today()).replace("-","")
    QUERY = "ALTER TABLE {} ADD COLUMN \"{}\" INTEGER(1) ".format(table, today)
    print(QUERY)
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(QUERY)
    con.commit()

def present(names = [],total = ["keegan", "rahil"] ,table = "attendance", database = "attendance.db"):
    today = str(date.today()).replace("-","")
    con = sqlite3.connect(database)
    cur = con.cursor()
    for i in total:
        if i not in names:
            QUERY = "UPDATE {} SET \"{}\" = 1  WHERE \"name\" =\"{}\"".format(table,today,i)
            cur.execute(QUERY)
        else:
            QUERY = "UPDATE {} SET \"{}\" = 0  WHERE \"name\" = \"{}\"".format(table,today,i)
            cur.execute(QUERY)
        con.commit()


def show_table(table = "attendance", database = "attendance.db"):
    con = sqlite3.connect(database)
    cur = con.cursor()
    QUERY = "SELECT * FROM {} ORDER BY name".format(table)
    for row in cur.execute(QUERY):
        print(row)
def return_columns(table = "attendance", database = "attendance.db"):
    con = sqlite3.connect(database)
    cur = con.cursor()
    QUERY = "PRAGMA table_info({});".format(table)
    k = [list(x)[1] for x in cur.execute(QUERY)]
    con.commit()
    return k

#adding_date()
#create_table()
#present()
#show_table()        
return_columns()
    
    



