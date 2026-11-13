import pandas as pd
import numpy as np
# CSV를 표로 불러오기
#df = pd.read_csv('data/12_metro_compressor.csv')
# 앞 5줄 (일반 .py 파일에서는 print 필요)
#print(df.head())

# 뒤에서5줄—기본
#df.tail()
# 뒤에서3줄만—숫자지정
#df.tail(3)
# → 파일끝깨짐·엉뚱한줄점검에필수
PATH = 'data/12_metro_compressor.csv'
df = pd.read_csv(PATH)
print(df.head())
print(df.tail())
print(df.head(3))
print(df.tail(10))

df.index
# RangeIndex(start=0, stop=200, step=1)
# 0부터 199까지 1씩 — 파일에 없던 번호를 read_csv가 붙여 준 것
len(df.index)     # 200 — shape의 앞 숫자와 같은 값

F = 'data/12_metro_digital.csv'
df = pd.read_csv(F)
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.head())

#df.info()
# RangeIndex: 200 entries
# 오일온도 199 non-null float64
# 모터전류 200 non-null float64
# shape와 달리 괄호 필요
A = 'data/12_metro_compressor.csv'
df_a = pd.read_csv(A)
print(df_a.info())
print("오일온도 NULL 1개")

print(df.describe())
#import pandas as pd
#df = pd.read_csv('data/12_metro_compressor.csv')
#print(df.describe().round(2))
# 오일온도 평균 63.18, 최대 75.0
# 숫자 열 5개를 한꺼번에 요약

#describe() 결과에 .loc[['원하는_통계치_이름']]을 사용하면 특정 행만 추출할 수 있다.
print(df_a.describe().loc[['mean']]) #mean만 골라서 출력
print(df_a.describe().loc[['50%']]) # 50%만 골라서 출력
print(df_a.describe().loc['mean']['모터전류'])
print(df_a.describe().loc['50%']['모터전류'])
print()
state = df_a['가동상태'].values #가동상태 열
cur = df_a['모터전류'].values # 모터전류 열
print(round(float(np.mean(cur[state == '가동'])), 2)) # 가동상태가 가동인 모터전류 값의 평균
print(round(float(np.mean(cur[state == '정지'])), 2)) # 가동상태가 정지인 모터전류 값의 평균
#df.describe(percentiles = [0.5]) #25%, 50%, 75% 중 50%만 포함시킨다.(min, max mean 전부 포함)


#PATH = 'data/12_metro_compressor.csv'
#df = pd.read_csv(PATH)
#A = 'data/12_metro_compressor.csv'
#df_a = pd.read_csv(A)
print(df.shape)
print(df_a.shape)
print("-"*20)
print(df.dtypes)
print(df_a.dtypes)
print("-*20")
print(df.info())
print(df_a.info())

#np.unique -> 중복된 값 제거
#arr = np.array(['apple', 'banana', 'apple', 'cherry', 'banana', 'apple'])
#values, counts = np.unique(arr, return_counts=True) -> 각 값의 빈도수 확인
b = df_a['모터전류'].values
print(np.unique(b, return_counts = True))

R = 'data/12_metro_small.csv'
r = pd.read_csv(R)
print(r.head())
print("-" * 20)
print(r.shape)
print('-' * 20)
print(r.info())
print("-" * 20)
miss = int(r["오일온도"].isna().sum()) #빈칸 확인
print(miss)
print("결측행: \n", r.shape[0] - r.count())
print("-" * 20)
print(round(r.describe().loc[['mean']],2))
print(round(r.describe().loc[['50%']],2))
print("자료 30행 7열, 결측 오일온도 1건, 모터전류 평균: 1.38, 모터전류 중앙값: 0.04")