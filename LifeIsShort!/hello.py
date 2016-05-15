print("happy")
print sorted(set('You need Python.'))[2]
print set('You need Python.')
print sorted(set('You need Python.'))

a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
print a.intersection(b) == a & b
print a.union(b) == a | b
print a.issubset(b)
print a.difference(b) == a - b

import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print a.shape


import numpy as np
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print a[[2]].sum()

from pandas import Series
sa = Series(['a', 'b', 'c'], index = [0, 1, 2])
sb = Series(['a', 'b', 'c'])
sc = Series(['a', 'c', 'b'])
print sa.equals(sc)
print sb.equals(sa)
print sa*3 + sc*2

from pandas import Series, DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print 'VS' in frame['IDE']

print frame.ix[2]
# language     Python
# year         ______
# IDE         IPython
# Name: 2, dtype: object


# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

##---(Sun May 01 10:35:10 2016)---
# runfile('C:/Users/sure GM/.spyder2/temp.py', wdir='C:/Users/sure GM/.spyder2')
# debugfile('C:/Users/sure GM/.spyder2/temp.py', wdir='C:/Users/sure GM/.spyder2')
# runfile('C:/Users/sure GM/.spyder2/temp.py', wdir='C:/Users/sure GM/.spyder2')
# help(seek)
# help(seek())
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers[0: -1]
# numbers[-2:]
# word = 'cloud'; print min(word)
# print 'Merry Xmas ' + 12.25
# [5] * 2
# help(str)
# str?
# help str
# dir(str)
# print '%05.3f' % math.pi
# 'Life is short, you need Python.'.find('you')
# seq = [1,2,3,4]
# sep = '+'
# sep.join(seq)
# seq.join(sep)
# print 'you' in 'Life is short, you need Python.'
# (1, 2) is zip(range(4), range(2,6))
# f = open('e:\\hello.txt', 'r')
# f
# f.seek(0,0)
# f.write('I am Yeliangchen')
# f = open('e:\\hello.txt', 'r')
# f.write('I am Yeliangchen')
# f = open('e:\\hello.txt', 'r+')
# f.write('I am Yeliangchen')
# f.readline()
# print f.readline()
# runfile('C:/Users/sure GM/.spyder2/temp.py', wdir='C:/Users/sure GM/.spyder2')
#
# ##---(Sun May 08 09:44:46 2016)---
# runfile('C:/Users/sure GM/.spyder2/temp.py', wdir='C:/Users/sure GM/.spyder2')
#
#
#
# import sys
# print(sys.version_info[0])
#
# if sys.version_info[0] == 3:
#     from urllib.request import urlopen
# else:
#     # Not Python 3 - today, it is most likely to be Python 2
#     # But note that this might need an update when Python 4
#     # might be around one day
#     from urllib2 import urlopen
#
# with urlopen("http://www.baidu.com/") as url:
#     s = url.read()
#
# print s
#