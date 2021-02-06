# coding=utf-8
import selenium
import requests
# from lxml import etree
import time

if __name__ == '__main__':
    class req_api():
        def get(self, url):
            self.req_url = url
            req = requests.get(self.req_url)
            return req


    url = 'https://cn.pornhub.com'
    # print(help('modules'))
    aa = req_api()
    rep = aa.get(url)

    print(rep.text)
