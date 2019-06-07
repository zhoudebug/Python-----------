import pymysql

def query_stu():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "SELECT * FROM Student"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        if not len(result):
            print("查无此人")
        for row in result:
            Sno = row[0]
            Sname = row[1]
            Sclass = row[2]
            print("Sno=%s,Sname=%s,Sclass=%s" % (Sno,Sname,Sclass))
    except:
        conn.rollback()
    conn.close()

# data_query("0914150230")


def query_teh():
    conn = pymysql.connect(host='192.168.123.209', user='root', passwd='123456', db='kaoqinxitong', charset='utf8')
    c = conn.cursor()
    sql_str = "SELECT * FROM Teacher"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        if not len(result):
            print("查无此人")
        for row in result:
            Tno = row[0]
            Tname = row[1]
            Tdept = row[2]
            print("Tno=%s,Tname=%s,Tdept=%s" % (Tno,Tname,Tdept))
    except:
        conn.rollback()
    conn.close()

def query_SC():
    conn = pymysql.connect(host='192.168.123.209', user='root', passwd='123456', db='kaoqinxitong', charset='utf8')
    c = conn.cursor()
    sql_str = "SELECT * FROM SC"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        if not len(result):
            print("查无此人")
        for row in result:
            Sno = row[0]
            Cname = row[1]
            print("Sno=%s,Cname=%s" % (Sno,Cname))
    except:
        conn.rollback()
    conn.close()

def query_Course():
    conn = pymysql.connect(host='192.168.123.209', user='root', passwd='123456', db='kaoqinxitong', charset='utf8')
    c = conn.cursor()
    sql_str = "SELECT Cname FROM Course"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        # print(result)
        if not len(result):
            print("查无此人")
        for row in result:
            Cname = row[0]
            print("Cname=%s" % (Cname))
    except:
        conn.rollback()
    conn.close()

def query_Cwa():
    conn = pymysql.connect(host='192.168.123.209', user='root', passwd='123456', db='kaoqinxitong', charset='utf8')
    c = conn.cursor()
    sql_str = "SELECT * FROM Cwa"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        # print(result)
        if not len(result):
            print("查无此人")
        for row in result:
            Sno = row[0]
            Tno = row[1]
            Cname = row[2]
            Cwa = row[3]
            ClassTime = row[4]
            Date = row[5]
            Time = row[6]
            print("Sno=%s,Tno=%s,Cname=%s,Cwa=%s,ClassTime=%s,Date=%s,Time=%s" % (Sno,Tno,Cname,Cwa,ClassTime,Date,Time))
    except:
        conn.rollback()
    conn.close()

query_stu()
query_teh()
query_SC()
query_Course()
query_Cwa()