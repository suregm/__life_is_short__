# import sys
# import urllib
#
# print(sys.version_info[0])


# import urllib
# for i in range(1000000000,1000000010):
#     web = urllib.urlopen('http://tieba.baidu.com/p/%d'%i)
#     html = web.read()
#     local = open(r'F:\%d.html'%i,'wb')
#     local.write(html)
#     local.close()


import urllib

for i in range(1000000000,1000000010):
    file_obj=open(r'F:\pythonCode\20160507\%d.txt'%i,mode='wb')
    context=urllib.urlopen('http://tieba.baidu.com/p/%d'%i)
    file_obj.write(context.read())
    file_obj.close()
    i+=1