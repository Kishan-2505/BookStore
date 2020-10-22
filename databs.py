import sqlite3

def create():

    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT,qty INTEGER,price REAL)")
    cur.execute("INSERT INTO store VALUES('gLASS',8,100.23)")
    conn.commit()
    conn.close()
def insert(item,qty,price):

    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
   
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,qty,price))
    conn.commit()
    conn.close()
#insert('coffee glass',10,5) 
def view():

    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    
    conn.close()   
    return rows
def delete(item):

    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
   
    conn.commit()
    conn.close() 
def update(qty,price,item):

    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET qty=?,price=? WHERE item=?",(qty,price,item))
    
    conn.commit()
    conn.close()    
update(8,40,'coffee glass')   
#delete('water glass')       
print(view())    