# QZFL.pluginsDefine.getACSRFToken._DJB = function(str) {
  #   var hash = 5381;
  #   for (var i = 0, len = str.length;i < len;++i) {
  #     hash += (hash << 5) + str.charCodeAt(i);
  #   }
  #   return hash & 2147483647;

'''
登录QQ空间，发现不是以POST请求来登录，因此，先登录然后复制cookie，之后用cookie来登录。
因为好友的说说列表是 js ajax 动态生成，无法返回说说列表信息。通过上网查资料 发现，说说的列表在
    emotion_cgi_msglist_v6
文件中，然后对其文件进行url设计访问，得到json格式数据，其中一个参数是g_tk 在另外一个js文件（qzfl_v8_...'）中
对其分析得出以上的g_tk表达式 求此g_k
'''

from urllib import parse
import re
from review import Tool

def get_cookie():
    '''Get cookie from cookie_file'''
    with open('cookie.txt','r') as f:
        cookie = f.read()
    cookie = cookie.replace('\n', '')
    return cookie

cookie = get_cookie()

headers = {'host': 'h5.qzone.qq.com',
            'User-Agent': Tool.Tool().getUser_Agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh,zh-CN;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': cookie,
            'connection': 'keep-alive'}

def get_g_tk():
    p_skey = re.findall('p_skey=(.*?);',cookie)[0]
    h = 5381

    for s in p_skey:
        h += (h << 5) + ord(s)

    return h & 2147483647

g_tk = get_g_tk()


#获取当前页面的信息
def parse_moods_url(qqnum,page=1):
    '''
        https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=173573018&ftype=0&sort=0&pos=0&num=20&
        replynum=100&g_tk=1096763595&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1
    '''

    params = {
              "relynum":100,
              "ftype":0,
              "code_version": 1,
              "format": "jsonp",
              "g_tk": g_tk,
              "hostUin": qqnum,
              "inCharset": "utf-8",
              "need_private_comment": 1,
              "notice": 0,
              "pos":(page-1)*20,
              "num": 20,
              "outCharset": "utf-8",
              "sort": 0,
              "replynum":100,
              "uin": qqnum
    }
    host = "https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?"

    url = host + parse.urlencode(params)
    return url