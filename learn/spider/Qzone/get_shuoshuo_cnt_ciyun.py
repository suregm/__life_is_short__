'''
获取所有说说 并存放在txt文本中
'''

import pymysql.cursors
import re

def get_cnt():
    f = open('E:/ScrapyData/Qzone/All_shuoshuos.txt','a',encoding='utf8')
    # 连接MySQL数据库
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',
                             db='qzone2', charset='utf8')
    # 通过cursor创建游标
    cursor = connection.cursor()
    sql = 'select content from shuoshuos'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        line = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\\%]", "", row[0])
        f.write(line)
    connection.commit()
    cursor.close()
    connection.close()
    f.close()

#get_cnt()

'''
 通过jieba分词
'''

import jieba.analyse as analyse

def get_jieba_shuoshuos():
    f_read = open('E:/ScrapyData/Qzone/All_shuoshuos.txt','r',encoding='utf8')
    f_keywords = open('key_words.txt','w',encoding='utf8')

    f_keywords.write('\t'.join(analyse.extract_tags(f_read.read(),200,withWeight=False)))
    f_read.close()
    f_keywords.close()






from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def get_ciyun():
    # Read the whole text.
    text = open("key_words.txt",'r',encoding='utf-8').read()

    # read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    qzone_coloring = np.array(Image.open("qzone.jpg"))

    # 设置停用词
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    # 你可以通过 mask 参数 来设置词云形状
    wc = WordCloud(background_color="white", max_words=200, mask=qzone_coloring,
                   stopwords=stopwords, max_font_size=150, random_state=100,width=2400,height=2400,font_path='C:\Windows\Fonts\simfang.ttf')
    # generate word cloud
    wc.generate(text)
    wc.to_file('E:/ScrapyData/Qzone/qzone.jpg')
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
    wc.to_file('E:/ScrapyData/Qzone/qzone2.jpg')

# get_jieba_shuoshuos()
get_ciyun()