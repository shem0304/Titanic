import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import count
import io

def rednooby_cralwler(input_search, filename):

    url = 'http://www.ksilbo.co.kr/news/articleList.html'

    post_dict = OrderedDict() #OrderedDict를 사용하여, key에 url 입력

    text = io.open(filename, 'w', encoding="utf-8")

    for pageStart in count(1): #1부터 무한대로 시작(break or return이 나올때까지)
        params = {
            'query' : input_search, #검색어를 사용자로부터 받아옴
            'sc_sub_section_code'    : 'S2N8',
            'view_type' : 'sm',
            'page' : pageStart,
        }

        response = requests.get(url, params =params)
        print(response.encoding)
        response.encoding = 'euc-kr'
        html = response.text

        #뷰티플소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #쪼개기
        #출처 : https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221177292446&proxyReferer=https%3A%2F%2Fwww.google.com%2F
        title_list = soup.select('td.ArtList_Title > div')
        print(title_list)
        for tag in title_list:
            #if tag['href'] in post_dict: #현재 저장할 링크(key)가 이미 post_dict에 있으면
            #    return post_dict #작업종료
            print(tag.text)
            tagStrLength = len(tag.text) - 11
            text.write(tag.text[0:tagStrLength])
            #post_dict[tag['href']] = tag.text
    text.close()
    return post_dict

rednooby_cralwler('울산+바이오', 'd:\\aihhi.txt')