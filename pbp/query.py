import pyodbc as db

#Query Virtuoso using an ODBC DSN
def query(x):
    x = x
    cnxn = db.connect("DSN=Local Virtuoso;UID=dba;PWD=dba")
    cursor = cnxn.cursor()
    cursor.execute(x)
    row = cursor.fetchall()
    if row:
        print(row)

def query_n1(x):
    try:
        x = x
        cnxn = db.connect("DSN=Local Virtuoso;UID=dba;PWD=dba")
        cursor = cnxn.cursor()
        cursor.execute(x)
    except db.ProgrammingError: 
        row = cursor.fetchall()
        if row:
            print(row)
    #if row:
    #    print(row)

#Query Virtuoso with Manual ODBC parameters
def query_nd(x):
        x = x
        cnxn = db.connect("DRIVER=/Library/ODBC/OpenLink Virtuoso ODBC Driver.bundle/Contents/MacOS/virtodbc_r.so; SERVER=localhost:1111;UID=username;PWD=password;WideAsUTF16=yes")
        cursor = cnxn.cursor()
        cursor.execute(x)
        row = cursor.fetchall()
        if row:
            print(row)