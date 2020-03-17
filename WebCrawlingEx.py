import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import count
import io
import collections

def rednooby_cralwler(maxpage, input_search, filename):

    url = 'https://search.naver.com/search.naver'

    post_dict = OrderedDict() #OrderedDict를 사용하여, key에 url 입력

    text = io.open(filename, 'w', encoding="utf-8")
    #text2 = io.open('D:\\articleinfo', 'w', encoding="utf-8")

    page = 1
    for page in count(1) : #1부터 무한대로 시작(break or return이 나올때까지)
        params = {
            'query' : input_search, #검색어를 사용자로부터 받아옴
            'sm'    : 'tab_jum',
            'where' : 'news',
            'start' : (page-1)*10+1,
        }
        response = requests.get(url, params =params)
        html = response.text

        #뷰티플소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #쪼개기
        title_list = soup.select('._sp_each_url._sp_each_title')

        for tag in title_list:
            #if tag['href'] in post_dict:  #현재 저장할 링크(key)가 이미 post_dict에 있으면
            #    break                     #작업종료
            print(tag.text)
            text.write(tag.text)
            #text2.write(str(len(post_dict))+', ' + tag.text+',  '+tag['href']+'\n\n')
            post_dict[tag['href']] = tag.text
            print('%s===> ' % len(post_dict))
        page += 1
        print('%s====>' % page)

    text.close()
    return post_dict

def main() :
    maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")
    query = input("검색어 입력: ")
    rednooby_cralwler(maxpage, query, 'd:\\aihhi.txt')

if __name__ == "__main__":
    main()
