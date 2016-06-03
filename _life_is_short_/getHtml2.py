__author__ = 'sure GM'

import urllib.request

for num in range(10):
    file = open('d:\\temp\\1000000000{}.html'.format(num), "wb")
    file.write(urllib.request.urlopen('http://tieba.baidu.com/p/100000000{}'.format(num)).read());
    file.close()
