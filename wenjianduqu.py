# coding=utf-8
import os, re
import sys  # new added

reload(sys)  # new added
sys.setdefaultencoding('utf-8')  # new addedimport sys # new added
print('origin_encoding = {}'.format(sys.getdefaultencoding()))
lj = r'D:\ziduan.txt'
# f=open(lj,'r',encoding='utf-8')
f = open(lj, 'r')
content = f.readlines()
f.close()
st = str(content)
lj2 = r'D:\ziduan2.txt'
# f=open(lj2,'r',encoding='utf-8')
f = open(lj2, 'r')
content2 = f.readlines()
print(unicode(content2))
f.close()
st2 = str(content2)
regex_str = "[\u4E00-\u9FA5]+"
match_obj = re.findall(regex_str, st)
match_obj2 = re.findall(regex_str, st2)
jieguo = []
jieguo2 = []
if match_obj:
    for ll in range(0, len(match_obj)):
        if match_obj[ll] not in match_obj2:
            jieguo.append(match_obj[ll])
            print
            match_obj[ll].encode('gb18030')
    print(jieguo)
if match_obj2:
    for ll in range(0, len(match_obj2)):
        if match_obj2[ll] not in match_obj:
            # print (match_obj2[ll])
            jieguo2.append(match_obj2[ll])
    print(jieguo2)
