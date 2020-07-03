import MySQLdb
from biliClass.biliAid import Aid
import time

def dblink():  # 连接数据库
    
    # demo
    return MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='password',
        db='nav',
        charset='utf8'
    )


def dbsql(conn, sql):  # 执行sql
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor


def dbclose(cursor, conn):  # 关闭sql与游标
    cursor.close()
    conn.commit()  # 好像不用这句也行？
    conn.close()


def insert(title, av_list):  # 插入av用，一次性插入
    conn = dblink()
    sql = """INSERT IGNORE INTO `nav_bili_v`
    (`id`, `av`, `bv`, `class`, `title`, `pic`, `descript`, `dynamic`, `o_name`, `o_face`, `s_view`, `s_danmaku`, `s_reply`, `s_like`, `s_coin`, `s_favorite`, `s_share`, `s_time`, `up`)
    VALUES """
    try:
        for av in av_list:
            sql += f"""(NULL, '{av}', NULL, '{title}', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),"""
        sql = sql[:-1]+';'  # python-str不可修改，这里是重赋值
        cursor = dbsql(conn, sql)
        dbclose(cursor, conn)
        print('【log: 插入成功】')
    except:
        print('【log: 插入失败】')


def read(where=''):  # 读取数据库
    if(where!=''):
        where = 'WHERE ' + where
    conn = dblink()
    sql = f"""SELECT * FROM `nav_bili_v` {where}"""
    cursor = dbsql(conn, sql)
    s = ''
    for row in cursor.fetchall():
        s = s + str(row) + '\n'
    dbclose(cursor, conn)
    return s



def autoUpdata(where=''):
    if(where!=''):
        where1 = 'WHERE ' + where
        where2 = 'AND ' + where
    conn = dblink()
    # 第一次处理sql语句 - 读取av列表
    sql_r = f"""SELECT * FROM `nav_bili_v` {where1}"""
    cursor = dbsql(conn, sql_r)
    av_list = cursor.fetchall()
    # 仅关闭游标以更新
    cursor.close()
    # 第二次处理sql语句 - 爬取信息并更新列表
    i = 0
    for row in av_list[:]:
        av = row[1]
        try:
            dic = Aid(av).dic
            time.sleep(0.3)  # 友善爬虫 && 防止被封ip
            sql_u = """UPDATE `nav_bili_v` """
            sql_u_temp = 'SET '
            for value in dic.values():
                for k,v in value.items():
                    sql_u_temp += f"`{k}`='{v[1]}',"
            sql_u_temp = f'''{sql_u_temp[:-1]} WHERE `av`={av} {where2}'''
            sql_u += sql_u_temp
            cursor = dbsql(conn, sql_u)
            print(f'[序列{i}] av:{av} 数据更新完毕')
        except:
            print(f'[序列{i}] av:{av} 数据更新失败!!!!!!!!!!!')
        i+=1
    print('\n数据表全部数据更新完毕')
    dbclose(cursor, conn)
