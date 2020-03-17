from datetime import time

import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import count
import io
import numpy as np
import pandas as pd
import os

def rednooby_cralwler(input_search, filename):

    print(input_search)
    url = 'https://search.naver.com/search.naver'

    post_dict = OrderedDict() #OrderedDict를 사용하여, key에 url 입력

    text = io.open(filename, 'a', encoding="utf-8")

    for page in range(1,2): #1부터 무한대로 시작(break or return이 나올때까지)
        params = {
            'query' : input_search, #검색어를 사용자로부터 받아옴
            'sm'    : 'tab_hty.top',
            'where' : 'nexearch',
            'start' : (page-1)*10+1,
        }
        print(page)
        response = requests.get(url, params =params)
        html = response.text

        #뷰티플소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

        #쪼개기
        title_Addr = ''
        #title_Addr = soup.select_one('.row > dd').string
        try:
            if soup.select_one('.txt_ellipsis') is not None :
                title_Addr = soup.select_one('.txt_ellipsis').string
                print('type1========================================================')
            elif soup.select_one('.row > dd') is not None:
                title_Addr = soup.select_one('.row > dd').text
                print('type2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            else:
                title_Addr = 'None'
                print('type3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            #title_Addr = soup.select('.row > dd ')

            print('ttt:', title_Addr)

                #for tag in title_Addr:
                #if tag['href'] in post_dict: #현재 저장할 링크(key)가 이미 post_dict에 있으면
                #    return post_dict #작업종료
            text.write(input_search+','+title_Addr+'\n')

            text.close()
        except:
            print('occured unknown error')

        return post_dict

def main() :
    base_dir = 'D:\\'
    excel_file = 'vendname.xlsx'
    excel_dir = os.path.join(base_dir, excel_file)

    # read a excel file and make it as a DataFrame
    df = pd.read_excel(excel_dir, # write your directory here
                                  sheet_name = '1',
                                  header = 0,
                                  na_values = 'NaN',
                                  thousands = ',',
                                  nrows = 508,
                                  comment = '#')
    for row in df.iterrows():
        rednooby_cralwler(row[1]['vname'], 'd:\\aihhi.txt')


if __name__ == "__main__":
    main()