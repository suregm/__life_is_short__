import requests
import json
from review.Qzone import get_emotionURL
import time
import pymysql.cursors
import re
from multiprocessing import Pool

# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                             db='qzone2', charset='utf8')
# 通过cursor创建游标
cursor = connection.cursor()

session = requests.session()

#获取当前页面的json信息
def get_current_pageData(qq,page):
    url = get_emotionURL.parse_moods_url(qq,page)
    print("访问链接："+url)
    headers = get_emotionURL.headers
    html =session.get(url,headers=headers)
    data = json.loads(html.text[10:-2])
    print("访问当前页面结束")
    return data

    #获取说说总数
def get_totalPage(qq):
    print("获取说说总数")
    data = get_current_pageData(qq,1)
    total = int(data['total'])
    if total%20==0:
        totalPage = int(total/20)
    else:
        totalPage = int(total/20) +1
    print("得到总数")
    return totalPage

    #获取说说的详细信息
def save_detailData(qq,data):
    shuoshuo = {}
    shuoshuo['number'] = qq
    shuoshuo['name'] = data['usrinfo']['name']
    msglist = data['msglist']
    for msg in msglist:
        shuoshuo['content'] = msg['content']
        #表示转载
        if('rt_con' in msg.keys()):
            shuoshuo['content_forward'] = msg['rt_con']['content']
            shuoshuo['is_forward'] = 1
        else:
            shuoshuo['content_forward'] = ""
            shuoshuo['is_forward'] = 0

        #时间戳 ,转换为 日期和时间 保存
        qq_created_time = msg['created_time']
        timeArray = time.localtime(qq_created_time)
        shuoshuo['date'] = time.strftime("%Y-%m-%d", timeArray)
        shuoshuo['time'] = time.strftime('%H:%M:%S',timeArray)
        #获取 发表说说的手机信息
        shuoshuo['phone'] = msg['source_name']
        #获取 说说评论数
        shuoshuo['cmtnum'] = msg['cmtnum']
        comment_name = []
        if(shuoshuo['cmtnum'] != 0):
            for comment in msg['commentlist']:
                comment_name.append(comment['name'])
        shuoshuo['cmtname'] = '---'.join(comment_name)
        #获取 发表 地点 、经纬度
        shuoshuo['location'] = msg['lbs']['idname']
        shuoshuo['pos_x'] = msg['lbs']['pos_x']
        shuoshuo['pos_y'] = msg['lbs']['pos_y']
        save_data_in_mysql(shuoshuo)
        print(shuoshuo)
    print("保存当页的信息")
    connection.commit()

def save_data_in_mysql(shuoshuo):
    sql = "INSERT INTO shuoshuos(number,name,content,is_forward,content_forward,date,time,phone,cmtnum,cmtname,location,pos_x,pos_y)  VALUES  ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')".format(shuoshuo['number'],shuoshuo['name'],shuoshuo['content'],shuoshuo['is_forward'],shuoshuo['content_forward'],shuoshuo['date'],shuoshuo['time'],shuoshuo['phone'],shuoshuo['cmtnum'],shuoshuo['cmtname'],shuoshuo['location'],shuoshuo['pos_x'],shuoshuo['pos_y'])
    try:
        cursor.execute(sql)
    except:
        return

def save_qq_in_mysql(qq,table_name):
    sql = "INSERT INTO "+table_name+"(qq) VALUES ('{}')".format(qq)
    cursor.execute(sql)

def get_all_page(qq):
    try:
        totalPage = get_totalPage(qq)
    except:
        print("无法访问 {} 的空间------>>>\n\n".format(qq))
        save_qq_in_mysql(qq,'fail')
        connection.commit()
        return
    for page in range(1,totalPage+1):
        print("爬取第 {0} 页 / {1} 页".format(page,totalPage))
        data = get_current_pageData(qq,page)
        save_detailData(qq,data)
        time.sleep(5)
    save_qq_in_mysql(qq,'success')
    print("爬取成功，存入数据库中------>>>\n\n")




if __name__=='__main__':
    start = time.time()
    p = Pool(4)
    f_qq = open('qqmail.txt','r')
    for line in f_qq.readlines():
        qq = re.findall('\d+',line)[0]
        print("开始爬取---->"+qq)
        p.apply_async(get_all_page,args=(qq,))
        time.sleep(5)
    f_qq.close()
    cursor.close()
    connection.close()
    session.close()
    p.close()
    p.join()
    end = time.time()
    print("\n\n爬完总共用时 ：{0:.2f} 分钟 ，即 {1:.2f} 小时".format((end-start)/60,(end-start)/3600))