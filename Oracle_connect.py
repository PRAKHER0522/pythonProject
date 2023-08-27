import cx_Oracle
username = 'HR'
password = 'HR'
host = 'localhost'
port = 1521
service_name = 'xe'

dsn=cx_Oracle.makedsn(host,port,service_name=service_name)

conn= cx_Oracle.connect(username,password,dsn)

if conn:
    print("Oracle HR database connected")
    cursor = conn.cursor()
    query = "select * from hr.employees"
    cursor.execute(query)

    for row in cursor:
        print(row)
    cursor.close()

conn.close()
