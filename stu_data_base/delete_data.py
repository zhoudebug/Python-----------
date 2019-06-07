import pymysql


def dele_stu(Sno):
    flag = True
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM Student WHERE Sno = '"+Sno+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
    # print("delete data success")

def dele_tch(Tno):
    flag = True
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM Teacher WHERE Tno = '"+Tno+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
    # print("delete data success")

def dele_SC(Sno,Cname):
    flag = True
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM SC WHERE Sno = '"+Sno+"' AND Cname ='"+Cname+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
    # print("delete data success")

def dele_Cname(Cname):
    flag = True
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM Course WHERE Cname = '"+Cname+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
    # print("delete data success")

def dele_CWA_Cwa(Sno,Cname,Time):
    flag = True
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM CWA WHERE Cname ='"+Cname+"' AND Sno = '"+Sno+"' AND Time='"+Time+"'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
    # print("delete data success")

def dele_Course_Cname(Cname):
    flag = True
    conn = pymysql.connect(host='192.168.123.209', user='root', passwd='123456', db='kaoqinxitong', charset='utf8')
    c = conn.cursor()
    sql_str = "DELETE FROM Course WHERE Cname ='" + Cname + "'"
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        flag = False
        conn.rollback()
    conn.close()
    if flag:
        return True
    else:
        return False
