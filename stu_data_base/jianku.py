import pymysql

conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
c = conn.cursor()

c.execute('''CREATE TABLE Student(
          Sno CHAR(10) PRIMARY KEY NOT NULL ,
          Sname CHAR(20) NOT NULL,
          Sclass CHAR(10) NOT NULL
)''')
conn.commit()

c.execute('''CREATE TABLE Teacher(
          Tno CHAR(10) PRIMARY KEY NOT NULL ,
          Tname CHAR(20) NOT NULL,
          Tdept CHAR(20) NOT NULL
)''')
conn.commit()

c.execute('''CREATE TABLE SC(
          Sno CHAR(10) NOT NULL,
          Cname CHAR(20) NOT NULL
)''')
conn.commit()

c.execute('''CREATE TABLE CWA(
          Sno CHAR(10) NOT NULL,
          Tno CHAR(10) NOT NULL,
          Cname CHAR(20) NOT NULL,
          Sclass CHAR(20) NOT NULL,
          Cwa CHAR(5) NOT NULL,
          ClassTime CHAR(10) NOT NULL,
          Date CHAR(20) NOT NULL,
          Time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

c.execute('''CREATE TABLE Course(
           Cname CHAR(20) NOT NULL
 )''')

# c.execute('''drop Table Cwa''')
conn.commit()

conn.close()

print("Create data base successfull!")
