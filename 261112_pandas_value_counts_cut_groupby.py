import pandas as pd
import numpy as np

#print(df["냉각기상태"].value_counts())
# 고장40 · 저하40 · 정상40 (동률의표시순서는다를수있음)
#print(df["밸브상태"].value_counts())
# 정상61 · 지연20 · 경미20 · 심각19 
#print(df["result"].value_counts())
# 정상67 · 고장53

#counts = df["result"].value_counts()
#ratios = df["result"].value_counts(normalize=True)
#print(counts) # 정상67 · 고장53
#print(ratios.round(3)) # 정상0.558 · 고장0.442
#print((ratios *100).round(1)) # 정상55.8 · 고장44.2 (%)
#결측까지하나의종류로포함하려면두옵션을함께지정합니다.
#print(df["result"].value_counts(
#normalize=True,dropna=False).round(3))

#dropna = False (결측도 하나의 종류로 포함)
#reindex 원하는 순서로 정렬
#sort = False 빈도수로 정렬하지 않음

FILE = 'data/14_hydraulic.csv'
READ = 'data/14_hydraulic_qc.csv'
df = pd.read_csv(FILE)
df_a = pd.read_csv(READ)
print(df.shape)
counts = df['밸브상태'].value_counts()
ratios = df['밸브상태'].value_counts(normalize = True)
print(counts)
print(round(ratios*100, 2),'%')
count = df['운전부하'].value_counts()
ratio = df['운전부하'].value_counts(normalize = True)
print(count)
print(round(ratio*100, 2),'%')
print("운전부하 최대 건수", max(count))
print("운전부하 최저 건수", min(count))
print("밸브상태 최대 건수", max(counts))
print("밸브상태 최저 건수", min(counts))

print('-' * 20)
print(df_a.shape)
check = df_a['검사결과'].value_counts()
check_r = df_a['검사결과'].value_counts(normalize = True)
print(check)
print(round(check_r, 3))
print(round(check_r, 3) * 100)

print('-' * 20)
#band =pd.cut(
# df["온도"],bins=[0,40,50,200],
#labels=["낮음","보통","높음"],right=True)
#print(band.value_counts(sort=False))
# 낮음41 · 보통40 · 높음39
# print("구간미지정:",band.isna().sum()) # 0
# print("검산:",band.value_counts().sum()) # 120

print(df['진동'].max(), df['진동'].min())
band = pd.cut(df['진동'], bins = [0, 0.6, 0.7, 1.0], labels = ['약함', '보통', '강함'], right = True)
print(band.value_counts(sort=False))
print("미지정", band.isna().sum())

#group by 기본 형태
# means = df.groupby("냉각기상태")["온도"].mean() - 줄 나누는 열 냉각기 상태, 숫자로 답할 열 온도
# print(means.round(2))
# 고장54.67 · 저하45.46 · 정상35.89 
# print(df.groupby("냉각기상태")["온도"].max())
# 고장57.8 · 저하51.2 · 정상36.4 
# print("평균차이:",round(means.loc["고장"]-means.loc["정상"],2))
# 18.78 —표시용반올림은계산을마친다음에적용
print(df.value_counts('냉각기상태'))
means = df.groupby("냉각기상태")['온도'].mean()
print(round(means, 2))
maxs = df.groupby("냉각기상태")['온도'].max()
print(round(maxs, 2))
print("온도차이", round(means.max() - means.min(), 2))

# keys =["냉각기상태","운전부하"]
# print(df.groupby(keys)["온도"].mean().round(2))
# 고장/고부하55.51 · 고장/저부하54.05
# 저하/고부하44.07 · 저하/저부하45.58
# 정상/고부하35.89
# print(df.groupby(keys).size())
# 17 · 23 · 3 · 37 · 40 (위그룹순서)
# 정상/저부하는0건이라이문자열열의groupby 결과에없음

#print(pd.crosstab(df["냉각기상태"],df["운전부하"]))
#    고부하저부하
# 고장17     23
# 저하 3     37
# 정상40      0
# print(pd.crosstab(df["밸브상태"],df["result"],
# normalize="index").round(3))
# # 각밸브상태안에서result 라벨비율을계산(각행의합≈ 1)
 
# mean_table =df.groupby(["냉각기상태","운전부하"])["온도"].mean()
# print(mean_table.unstack().round(2))
# 정상/저부하는NaN: 0℃가아니라측정행이없어평균을계산못함

valv = df.value_counts('밸브상태')
print(valv)
error = df[df['result'] == '고장']
error_count = error.value_counts('밸브상태')
print(error_count)
error_count =pd.crosstab(df['밸브상태'], df['result'])
error_per =pd.crosstab(df['밸브상태'], df['result'], normalize = "index") #index는 비율 표시
print(error_count)
print(round(error_per, 3))