import numpy as np
import pandas as pd
import os
from matplotlib import font_manager, rc
import matplotlib
import matplotlib as plt

base_dir = 'd:\\'
excel_file = 'ntis.xls'
excel_dir = os.path.join(base_dir, excel_file)

df_from_excel = pd.read_excel(excel_dir, sheet_name='검색결과', usecols=['NO', '기준년도'])
print(df_from_excel)

df_basicYear = df_from_excel.groupby('기준년도').count()

print(df_basicYear)

font_location = "c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
#df_basicYear.plot(x=)