import re
import requests

# def get_songid():
#   """获取音乐的songid"""
#   url = 'http://music.taihe.com/artist/2517'
#   response = requests.get(url=url)
#   html = response.text
#   sids = re.findall(r'href="/song/(\d+)" rel="external nofollow" ', html)
#   return sids
music_url='http://audio04.dmhmusic.com/71_53_T10045968308_128_4_1_0_sdk-cpm/cn/0209/M00/63/C3/ChR47FsYZ2-AdPDoAD62g6ZmqJ4302.mp3?xcode=a692d613a896fc5b6791f54c4341677eb034951'
response = requests.get(music_url)
content = response.content
filename='test_text.mp3'
with open(file=filename, mode="wb") as f:
    f.write(content)
