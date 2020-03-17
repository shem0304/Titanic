from collections import Counter
from konlpy.tag import Twitter, Okt
import pytagcloud
import matplotlib.pyplot as pp
from matplotlib import font_manager, rc
import matplotlib
import webbrowser
import io, os
from collections import OrderedDict

#출처 : https://ericnjennifer.github.io/python_visualization/2018/01/21/PythonVisualization_Chapt3.html

# 각 크롤링 결과 저장하기 위한 리스트 선언
title_text = []

def showGraph(wordInfo):
    currentPath = os.getcwd()
    print(currentPath)
    try :
        font_location = "c:\\Windows\\fonts\\malgun.ttf"
        font_name = font_manager.FontProperties(fname=font_location).get_name()
        matplotlib.rc('font', family=font_name)

        pp.title('뉴스 검색 결과 빈도 분석')
        pp.xlabel('주요 단어')
        pp.ylabel('빈도수')
        pp.grid(True)

        Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)
        Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True)

        pp.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')
        pp.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')

        pp.show()
    except Exception as e:
        print('Exception Error.', e)

# 출처 : https://thinkwarelab.wordpress.com/2016/08/30/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%98%95%ED%83%9C%EC%86%8C-%EB%B6%84%EC%84%9D%EC%9C%BC%EB%A1%9C-%EC%9B%8C%EB%93%9C%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C-%EA%B7%B8%EB%A6%AC%EA%B8%B0/

def saveWordCloud(wordInfo, filename):
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=100)
    pytagcloud.create_tag_image(taglist, filename, size=(700, 480), fontname='korean', rectangular=False)
    webbrowser.open(filename)

def DrawGrap(atags):

    post_dict = OrderedDict() #OrderedDict를 사용하여, key에 url 입력
    text = io.open('d:\\aihhi.txt', 'a', encoding="utf-8")
    #text2 = io.open('D:\\articleinfo', 'a', encoding="utf-8")
    for tag in atags:
        if tag['href'] in post_dict:  #현재 저장할 링크(key)가 이미 post_dict에 있으면
            break                     #작업종료
        print(tag.text)
        text.write(tag.text)
        #text2.write(str(len(post_dict))+', ' + tag.text+',  '+tag['href']+'\n\n')
        post_dict[tag['href']] = tag.text
        print('%s===> ' % len(post_dict))
    text.close()
    return post_dict


def main():
    f = open('d:\\aihhi.txt', 'r', encoding="utf-8")

    data = f.read()

    print(data)

    nlp = Okt()
    nouns = nlp.nouns(data)
    print(nouns)
    count = Counter(nouns)

    removewords = ['년도', '대한', '통한', '통해', '사용자', '내용', '위해', '개발']
    #그래프
    wordInfo = dict()
    for tags, counts in count.most_common(50):
        if (len(str(tags)) > 1) and not tags in (removewords):
            wordInfo[tags] = counts
            print("%s : %d" % (tags, counts))

    showGraph(wordInfo)
    saveWordCloud(wordInfo, 'd:\\aiwordcloud.jpg')

    #print(count)
    #tag2 = count.most_common(50)
    #taglist = pytagcloud.make_tags(tag2, maxsize=150)
    #print(taglist)
    #pytagcloud.create_tag_image(taglist, 'd:\\aiwordcloud.jpg', size=(900, 600), fontname='korean', rectangular=False)
    #fileName = 'd:\\aiwordcloud.jpg'
    #ndarray = img.imread(fileName)
    #pp.imshow(ndarray)
    #pp.show()

if __name__ == "__main__":
    main()