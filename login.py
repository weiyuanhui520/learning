#coding=utf-8
from selenium import webdriver
from time import sleep
import codecs
'''定义全局变量'''
def webinfo():
    xx = open(r'C:\Users\HP\Desktop\login\xinxi.txt')
    zd={}
    for key in xx:
       zhuanhuan=key.split('=')
       zhuanhuan2=[ele.strip() for ele in zhuanhuan]
       zd.update(dict([zhuanhuan2]))
    xx.close()
    return zd

def userinfo():
    yy=open(r'C:\Users\HP\Desktop\login\zhangmi.txt')
    zd={}
    lt=[]
    for zm in yy:
        jj=zm.split(' ')
        jj2=[ nn.strip()for nn in jj]
        jj3=[kk.split('=') for kk in jj2]
        zd.update(dict(jj3))
        lt.append(zd)
        print lt
    return lt

'''打开浏览器'''
def openweb ():
    handle=webdriver.Chrome()
    return handle

'''打开网址'''
def getweb(handle,wz):
    handle.get(wz['wz'])
    sleep(1)
    handle.maximize_window()
    #return handle

'''查找元素'''
def findele(handle,arg):
    clk=handle.find_element_by_id(arg['anniu'])
    clk.click()
    sleep(1)
    ifra=handle.find_elements_by_tag_name('iframe')
    handle.switch_to.frame(ifra[0])
    sleep(0.5)
    acount=handle.find_element_by_name(arg['acount'])
    passwd=handle.find_element_by_name(arg['passwd'])
    denglu=handle.find_element_by_id(arg['denglu'])
    return acount,passwd,denglu




def sendval(findele,arg):
    lt=['zhanghu','mima']
    i=0
    for info in lt:
        findele[i].send_keys('')
        findele[i].clear()
        findele[i].send_keys(arg[0][info])
        i+=1
        print arg[0][info]
    findele[2].click()




if __name__=='__main__':
    wi=webinfo()
    ui=userinfo()
    #print ui
    op=openweb()
    getweb(op,wi)
    tu=findele(op,wi)
    sendval(tu,ui)



