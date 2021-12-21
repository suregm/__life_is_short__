from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import pymysql
import random

def get_my_friend():
    f = open('E:/ScrapyData/Qzone/All_shuoshuos.txt','a',encoding='utf8')
    # 连接MySQL数据库
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                             db='qzone2', charset='utf8')
    # 通过cursor创建游标
    cursor = connection.cursor()
    sql = 'select cmtname from shuoshuos where number=173573018'
    cursor.execute(sql)
    rows = cursor.fetchall()
    str = ''
    last=''
    for row in rows:
        names = row[0]
        for name in names.split('---'):
            a = name
            if(name==""):
                continue
            if(last == name):
            #因为jieba分词会将连续出现的两个人名以为成一个
                name = name+random.choice('abcdefg')
            str = str+'\t\t'+name
            last = a
    f =open('E:/ScrapyData/Qzone/my_friend.txt','w',encoding='utf8')
    f.write(str)
    f.close()

def get_myfriend_pic():
    # Read the whole text.
    text = open("E:/ScrapyData/Qzone/my_friend.txt",'r',encoding='utf-8').read()
    a = text.replace("大类",'').replace('软工','').replace('信计','').replace('信管','').replace('七班','').replace('em','').replace("-",'').replace("14","").replace("13","")
    # read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    print(a)
    qzone_coloring = np.array(Image.open("friend_logo.jpg"))

    # 设置停用词
    stopwords = set(STOPWORDS)
    stopwords.add("大类")
    stopwords.add("软工")
    stopwords.add("信计")
    stopwords.add("信管")
    stopwords.add("七班")
    stopwords.add("em")

    # 你可以通过 mask 参数 来设置词云形状
    wc = WordCloud(background_color="white", max_words=300, mask=qzone_coloring,
                   stopwords=stopwords, max_font_size=150, random_state=42,width=2400,height=2400,font_path='C:\Windows\Fonts\simfang.ttf')
    # generate word cloud
    wc.generate(a)
    wc.to_file('E:/ScrapyData/Qzone/myfriend.png')
    # create coloring from image
    image_colors = ImageColorGenerator(qzone_coloring)

    # show
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off") #去掉线框

    plt.figure()  #产生一个figure
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    # 我们还可以直接在构造函数中直接给颜色
    # 通过这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure('b')
    plt.imshow(qzone_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    wc.to_file('E:/ScrapyData/Qzone/myfriend2.png')
# get_my_friend()
get_myfriend_pic()