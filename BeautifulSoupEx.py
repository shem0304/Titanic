from lxml.html import parse
from bs4 import BeautifulSoup
import urllib3


http = urllib3.PoolManager()

url = 'https://www.udi.re.kr/bbs/board.php?bo_table=research_report'
response = http.request('GET', url)
soup = BeautifulSoup(response.data)

res = soup.find_all('div','ft14 bb hidden-xs')

print(res)

