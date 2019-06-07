import pymysql


def data_stu_Sclass_update(Sno,Sclass):
    stat = 0
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "UPDATE Student SET Sclass = '"+Sclass+"' WHERE Sno ='"+Sno+"'"
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        conn.rollback()
        stat = 1
    conn.close()
    if stat:
        return 1
    else:
        return 0


def data_stu_Sname_update(Sno,Sname):
    stat = 0
    conn = pymysql.connect(host = '192.168.123.209',user = 'root',passwd = '123456',db = 'kaoqinxitong',charset = 'utf8')
    c = conn.cursor()
    sql_str = "UPDATE Student SET Sname = '"+Sname+"' WHERE Sno ='"+Sno+"'"
    try:
        c.execute(sql_str)
        conn.commit()
    except:
        conn.rollback()
        stat = 1
    conn.close()
    if stat:
        return 1
    else:
        return 0

# data_stu_Sname_update("0914150225","于乐乐")