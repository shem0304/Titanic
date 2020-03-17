from collections import Counter

import konlpy
from konlpy.tag import Twitter, Okt
import pytagcloud
import matplotlib.image as img
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib
import webbrowser
import wordcloud
from wordcloud import WordCloud
from os import path

#출처 : https://ericnjennifer.github.io/python_visualization/2018/01/21/PythonVisualization_Chapt3.html
def showGraph(wordInfo):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.title('울산 인공지능 뉴스 검색 결과')
    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)

    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

    plt.show()

# 출처 : https://thinkwarelab.wordpress.com/2016/08/30/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EC%9C%BC%EB%A1%9C-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B7%B8%EB%A6%AC%EA%B8%B0/

def saveWordCloud(Noun_words, filename):
    taglist = pytagcloud.make_tags(dict(Noun_words).items(), maxsize=30)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='korean', rectangular=False)
    webbrowser.open(filename)

def main():
    f = open('d:\\aihhi.txt', 'r', encoding="utf-8")

    content = f.read()

    filtered_content = content.replace('.', '').replace(',', '').replace("'", "").replace('·', ' ').replace('=','').replace('\n', '')

    # 형태소 분석
    Okt = konlpy.tag.Okt()
    Okt_morphs = Okt.pos(filtered_content)
    #print(Okt_morphs)

    # 명사, 조사 네이밍 표현 다시 변경
    komoran = konlpy.tag.Komoran()
    komoran_morphs = komoran.pos(filtered_content)

    # 명사만 추출
    Noun_words = []
    for word, pos in Okt_morphs:
        if pos == 'Noun':
            Noun_words.append(word)
    #print(Noun_words)

    # 불용어 제거용 사전 구축
    removewords = ['바이오','산업', '위해','방문','부처','등','처', '한국']
    unique_Noun_words = set(Noun_words)
    for word in unique_Noun_words:
        if word in removewords:
            while word in Noun_words: Noun_words.remove(word)

    # 빈도분석
    count = Counter(Noun_words)

    #그래프
    wordInfo = dict()
    for tags, counts in count.most_common(30):
        if (len(str(tags)) > 1):
            wordInfo[tags] = counts
            print("%s : %d" % (tags, counts))

    showGraph(wordInfo)
    saveWordCloud(Noun_words, 'd:\\aiwordcloud.jpg')

if __name__ == "__main__":
    main()