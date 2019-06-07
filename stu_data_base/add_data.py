import pymysql

def add_stu(Sno,Sname,Sclass):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    stat = True
    c = conn.cursor()
    sql_str = "INSERT INTO Student (Sno,Sname,Sclass) VALUES ('"+Sno+"','"+Sname+"','"+Sclass+"') "
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        stat = False
        conn.rollback()
    conn.close()
    if stat:
        return True
    else:
        return False
    # print("Add data success")

# add_stu("0914150225","张飞","09141502")


# def add_teh(Tno,Tname,Tdept):
#     conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
#     stat = True
#     c = conn.cursor()
#     sql_str = "INSERT INTO Teacher (Tno,Tname,Tdept) VALUES ('"+Tno+"','"+Tname+"','"+Tdept+"') "
#     try:
#         c.execute(sql_str)
#         conn.commit()
#     except:
#         conn.rollback()
#         stat = False
#     conn.close()
#     if stat:
#         return True
#     else:
#         return False
#     # print("Add data success")

def add_SC(Sno,Cname):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    stat = True
    c = conn.cursor()
    sql_str = "INSERT INTO SC (Sno,Cname) VALUES ('"+Sno+"','"+Cname+"') "
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        stat = False
        conn.rollback()
    conn.close()
    if stat:
        return True
    else:
        return False

def add_Course_Cname(Cname):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    stat = True
    c = conn.cursor()
    sql_str = "INSERT INTO Course (Cname) VALUES ('" + Cname + "') "
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        stat = False
        conn.rollback()
    conn.close()
    if stat:
        return True
    else:
        return False

def add_CWA(Sno,Tno,Cname,Sclass,Cwa,Class_time,Date):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    stat = True
    c = conn.cursor()
    sql_str = "INSERT INTO CWA (Sno,Tno,Cname,Sclass,Cwa,ClassTime,Date) VALUES ('"+Sno+"','"+Tno+"','"+Cname+"','"+Sclass+"','"+Cwa+"','"+Class_time+"','"+Date+"') "
    print(sql_str)
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        stat = False
        conn.rollback()
    conn.close()
    if stat:
        return True
    else:
        return False

def add_teh(Tno,Tname,Tdept):
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong')
    stat = True
    c = conn.cursor()
    sql_str = "INSERT INTO Teacher (Tno,Tname,Tdept) VALUES ('"+Tno+"','"+Tname+"','"+Tdept+"') "
    c.execute(sql_str)
    conn.commit()
    conn.rollback()
    stat = False
    conn.close()
    if stat:
        return True
    else:
        return False
    # print("Add data success")
