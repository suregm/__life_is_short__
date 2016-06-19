__author__ = 'sure GM' '2016/5/20 0:24'

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print a.mean()

sure = "good"
print(sure + 'boy')


def fib(n):
    a, b = 0, 1
    count = 1
    while count  < n:
        a, b = b, a+b
        count = count + 1

print(fib(2))


l = [1,2,3,4]
l.reverse()
print(l)

l = [1,2,3,4]
l[len(l):] = [7]
print l
l.append(9)
print l



l.insert(2,-1)
print(l)
for i in reversed(l):
    print i
for i in enumerate(l):
    print i

l = [1,2,3,4]
l.pop()
print(l)
print(l.index(3))

scores = {'Jack': 90, 'Mike': 80, 'Jay': 85, 'Bill': 60}
print(sorted(scores.keys()))
for k, v in scores.items():
    print k, v

print((1, 2, 3, 4) < (1, 2, 4))


def f(x):
     global a
     a = 7
     print a + x,

a = 5
f(8)
print  a



import numpy as np; matrix = np.ones((3, 4))
print(matrix)


print range(2,7)


def go(x):
    if(x[:] == x[::-1]):
        print True
    else:
        print False

go("goog")
go("good")



print(list(reversed(range(1, 10, 2)))[2])


a = {1, 2, 3, 4}
b = {2, 3, 5, 6}
print(b-a)





t = (1, 2.0, 'hello')
print t == ('hello', 1, 2.0)






