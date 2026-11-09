import numpy as np
import pandas as pd

#pandas
# 표 형태의 데이터를 잘 다루기 위해
# series = 하나의 열들
# DataFrame - Series가 모여서 합쳐진 것, 표 구조 (df)

path = r"C:\Users\coco\Desktop\posco\data\12_metro_compressor.csv"
df = pd.read_csv(path)

#F = 'data/12_metro_compressor.csv'      # 오일온도는 왼쪽에서 다섯 번째 열
# 08 파트 방식 — csv 모듈
#import csv
#oil = []
#with open(F, encoding='utf-8') as f:
#    reader = csv.reader(f)
#    next(reader)                        # 헤더를 직접 걷어냄
#    for row in reader:
#        oil.append(float(row[4]) if row[4] else None)
# 11 파트 방식 — NumPy 배열
#import numpy as np
#oil = np.genfromtxt(F, delimiter=',', skip_header=1, usecols=4)
# 12 파트 방식 — Pandas
#import pandas as pd
#oil = pd.read_csv(F)['오일온도']

#import pandas as pd     # 앞 단원의 np 와 같은 별명 약속
# CSV를 DataFrame으로 — 분석의 시작
#df = pd.read_csv("data/12_metro_compressor.csv")
#df.head() - DataFrame으로
print("데이터 크기:", df.shape)
print(df.head())
print("열이름 : ", df.columns.to_list()) #열이름 출력
print("데이터 타입: ", df.dtypes)
state = df["가동상태"].values
print("가동상태 개수:",state)
print("가동상태 종류 개수: ",np.unique(state, return_counts = True))
cur = df["모터전류"].values
s = df["오일온도"]
print(s.head(3))
print("모터전류 평균 %.2f /  가운대 값 %.2f" % (np.mean(cur), np.median(cur)))

def col(i):
    return pd.read_csv(path, sep = ',', usecols = i, encoding = 'utf-8')
name = col(["측정시각", "오일온도", "모터전류"])
print(name.shape)

def col(i):
    return pd.read_csv(path, sep = ',', usecols = i, encoding = 'utf-8', nrows = 5)
name = col(["측정시각", "오일온도", "모터전류"])
print(name)

file = r"C:\Users\coco\Desktop\posco\data\12_metro_compressor_semicolon.csv"
define = pd.read_csv(file)
print(define)
define = pd.read_csv(file, sep = ';', encoding = 'utf-8')
print(define)

#import pandas as pd
# 엑셀 파일도 거의 같은 방식 — 시트 이름만 더 지정
# x = pd.read_excel('data/예시_설비로그.xlsx', sheet_name='2월')
# 분석한 결과를 파일로 남기기
#df = pd.read_csv('data/12_metro_compressor.csv')
#sel = df[['측정시각', '오일온도', '모터전류']]
#sel.to_csv('out_selected.csv', index=False, encoding='utf-8-sig')
# index=False        붙여 준 번호는 저장하지 않음
# encoding='utf-8-sig'  엑셀로 열어도 한글이 안 깨

define = pd.read_csv(file, sep = ';', encoding = 'utf-8', usecols = ["측정시각", "오일온도", "모터전류"], nrows = 50)
print(define)
print(define.shape)