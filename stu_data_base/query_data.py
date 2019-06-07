import pymysql


def Stu_data_query(Sno):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "SELECT * FROM Student WHERE Sno ='"+Sno+"'"
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


def Stu_Sclass_query(Sno):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Sclass = []
    sql_str = "SELECT Sclass FROM Student WHERE Sno ='"+Sno+"'"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        if not len(result):
            print("查无此人")
        for row in result:
            Sclass.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Sclass


def SC_Cname_Query(Sno):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Cname = []
    sql_str = "SELECT Cname FROM SC WHERE Sno ='" + Sno + "'"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Cname.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Cname


def Course_Cname_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Cname = []
    sql_str = "SELECT Cname FROM Course"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Cname.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Cname

def Teacher_Tno_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Tno = []
    sql_str = "SELECT Tno FROM Teacher"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Tno.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Tno


def Teacher_Tname_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Tname = []
    sql_str = "SELECT Tname FROM Teacher"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Tname.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Tname


def Student_Sno_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Sno = []
    sql_str = "SELECT Sno FROM Student"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Sno.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Sno

def Cwa_Cname_Query(Sno):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Cname = []
    sql_str = "SELECT DISTINCT Cname FROM CWA WHERE Sno='"+Sno+"'"
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Cname.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Cname

def Cwa_Time_Query(Sno,Cname):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Time = []
    sql_str = "SELECT Time FROM CWA WHERE Sno ='"+Sno+"' AND Cname ='"+Cname+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Time.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Time

def SC_Student_Class_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Sclass = []
    sql_str ="SELECT DISTINCT Sclass FROM Student,SC WHERE SC.Sno = Student.Sno"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Sclass.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Sclass

def CWA_Date_Query():
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Date = []
    sql_str ="SELECT DISTINCT Date FROM CWA"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Date.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Date

def CWA_Cname_Query(Sclass):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    Cname = []
    sql_str ="SELECT DISTINCT Cname FROM CWA WHERE Sclass = '"+Sclass+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            Cname.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return Cname

def CWA_ClassTime_Query(Sclass,Date):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    ClassTime = []
    sql_str ="SELECT DISTINCT ClassTime FROM CWA WHERE Sclass = '"+Sclass+"' AND Date = '"+Date+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
        for row in result:
            ClassTime.append(row[0])
    except:
        conn.rollback()
    conn.close()
    return ClassTime

def CWA_Message_Query(Sclass,ClassTime,Date,Cname):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str ="SELECT * FROM CWA WHERE Sclass = '"+Sclass+"' AND ClassTime = '"+ClassTime+"' AND Date ='"+Date+"'AND Cname='"+Cname+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        # conn.commit()
        # print (c.fetchall())
        result = c.fetchall()
    except:
        conn.rollback()
    conn.close()
    return result