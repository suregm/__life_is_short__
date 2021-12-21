'''
获取说说发表时间存入excel中
'''

import pymysql.cursors
import xlwt

'''
获取和统计 每个时段、每个月、每年 说说发表的总量
'''
def get_cnt():
    f = open('E:/ScrapyData/Qzone/All_shuoshuos.txt','a',encoding='utf8')
    # 连接MySQL数据库
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                             db='qzone2', charset='utf8')
    # 通过cursor创建游标
    cursor = connection.cursor()
    sql = 'select time,date from shuoshuos'
    cursor.execute(sql)
    rows = cursor.fetchall()
    time = [0]*24
    date_year = [0]*10
    date_month = [0]*13
    for row in rows:
        hour = int(str(row[0]).split(":")[0])
        year = int(str(row[1])[:4])-2008
        month = int((str(row[1])[5:7]))
        date_year[year]+=1
        date_month[month]+=1
        time[hour]+=1
    print(time)
    print(date_year)
    print(date_month)


    connection.commit()
    cursor.close()
    connection.close()
    f.close()


    # 创建 xls 文件对象
    wb = xlwt.Workbook()
    # 新增表单
    s_t = wb.add_sheet('time')
    s_y = wb.add_sheet('date')
    s_m = wb.add_sheet('month')
    # 按位置添加数据
    for t in range(len(time)):
        s_t.write(0,t , t)
        s_t.write(1, t, time[t])

    for y in range(len(date_year)):
        s_y.write(0,y,2008+y)
        s_y.write(1,y,date_year[y])

    for m in range(1,len(date_month)):
        s_m.write(0,m-1,m)
        s_m.write(1,m-1,date_month[m])
    # 保存文件
    wb.save('E:/ScrapyData/Qzone/chart.xls')

get_cnt()