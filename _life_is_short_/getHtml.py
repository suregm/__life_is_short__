import urllib

__author__ = 'sure GM'

def get_html(url, i):
    response = urllib.urlopen(url)
    htmlfile = response.read()
    f = open(r'd:\100000000' + str(i) +'.html', 'wb')
    f.write(htmlfile)
    f.close()

for i in range(10):
    url = 'http://tieba.baidu.com/p/100000000' + str(i)
    get_html(url, i)