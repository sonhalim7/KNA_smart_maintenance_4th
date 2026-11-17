import numpy as np
import pandas as pd

FILE = 'data/16_diecasting.csv'
df = pd.read_csv(FILE)
READ = 'data/16_welding.csv'
df_w = pd.read_csv(READ)
# Q1 = 25%, Q2 = 50% (= 중앙값), Q3 = 75%
#Q1 = df["temperature"].quantile(0.25)
#Q2 = df["temperature"].quantile(0.5)
#Q3 = df["temperature"].quantile(0.75)
#print(Q1, Q2, Q3)
# 결과: 74.0 76.5 81.5
# 대괄호로묶어세값한번에
#print(df["temperature"].quantile([0.25, 0.5, 0.75]))

#25·50·75를넣는경우—오류 quantile 인자는 반드시0~1 소수. 25를넣으면오류

#print(df["temperature"].describe()) # 분포 요약 통계를 한번에 표시

print(df.head())
print('자료형:', df.shape)
print("열이름:", df.columns)
print(df.info())

cyl = df['실린더압력']
print("최댓값:", cyl.max())
print("최소값:", cyl.min())
print("범위:", cyl.max() - cyl.min())
print('-' * 20)
time_line = df['사이클타임'].sort_values(ascending = False)
print(time_line) #6170 값 확인
error = time_line[(time_line > 35) | (time_line < 20)]
good = time_line[(time_line <= 35) & (time_line >= 20)]

print("정상값", good)
print("이상값", error)

print('-' * 20)
time_mean = round(df['사이클타임'].mean(), 2)
time_median = df['사이클타임'].median()

time_good = df.loc[df['상태'] == 0, '사이클타임']
time_good_mean = time_good.mean()
print("전체 평균:", time_mean)
print("전체 중앙값:", time_median)
print("정상값 평균:", round(time_good_mean, 2))

print('-' * 20)
Q1 = df["실린더압력"].quantile(0.25)
Q2 = df["실린더압력"].quantile(0.5)
Q3 = df["실린더압력"].quantile(0.75)
cyl_median = df['실린더압력'].median()
print(Q2, cyl_median)

print('-' * 20)
pres = df["주조압력"].describe()
shape = df["형체력"].describe()
time = df["사이클타임"].describe()
thick = df["비스킷두께"].describe()
cyl_pres = df['실린더압력'].describe()
print(pres)
print(shape)
print(time)
print(thick)
print(cyl_pres)
cols =['주조압력', '실린더압력', '사이클타임', '형체력', '비스킷두께']
desc = df[cols].describe()
summary = pd.DataFrame({'평균' : desc.loc['mean'],
                        "중앙값" : desc.loc['50%']})
summary['차이'] = abs(summary['평균'] - summary['중앙값'])
summary_sort = summary.sort_values(by = '차이', ascending = False)
print(summary_sort)

print('-' * 20)

Q1_cyl = df["실린더압력"].quantile(0.25)
Q2_cyl = df["실린더압력"].quantile(0.5)
Q3_cyl = df["실린더압력"].quantile(0.75)

Q1_time = df["사이클타임"].quantile(0.25)
Q2_time = df["사이클타임"].quantile(0.5)
Q3_time = df["사이클타임"].quantile(0.75)

Q1_thi = df["비스킷두께"].quantile(0.25)
Q2_thi = df["비스킷두께"].quantile(0.5)
Q3_thi = df["비스킷두께"].quantile(0.75)

cyl_width = Q3_cyl - Q1_cyl #IQR
time_width = Q3_time - Q1_time
thi_width = Q3_thi - Q1_thi
print("실린더압력 폭", round(cyl_width, 2))
print("사이클타임 폭", round(time_width, 2))
print("비스킷두께 폭", round(thi_width, 2))

#IQR = Q3 - Q1 정상 범위 최대 :Q3 + (1.5 X IQR), 최소: Q3 - (1.5 X IQR) 
#Q1 = df["temperature"].quantile(0.25)
#Q3 = df["temperature"].quantile(0.75)
#IQR = Q3 -Q1
#lower = Q1 -1.5 * IQR
#upper = Q3 + 1.5 * IQR
#print(lower, upper)

#조건으로 이상치 골라내기
#mask = (df["temperature"] < lower) | (df["temperature"] > upper)
#print(mask.sum())
#print(df[~mask].shape)

#이상치 개수와 비율
#print(mask.sum())
#print(round(mask.mean() * 100, 1)

#이상치 제거
#df_clean = df[~mask]
#print(len(df), len(df_clean))
#print(df_clean["temperature"].mean())

#경계값으로 보정
#df["temp_clipped"] = df["temperature"].clip(lower=lower, upper=upper)
#print(df["temp_clipped"].min())
#print(df["temp_clipped"].max())
#print(df["temp_clipped"].mean())

#결측치로 바꿔 채우기 -> 이상치 값을 NAN으로 바꾼다. -> 중앙값으로 채운다.(주변과 어울리는 값)
#masked = df["temperature"].mask(mask)
#print(masked.isna().sum())
#med = masked.median()
#fixed = masked.fillna(med)
#print(fixed.mean())

#duplicated -> 중복찾기(중복이 앞에 있었으면 TRUE, 없으면 FALSE 첫 값은 중복이 있어도 무조건 FALSE로 나온다.)
#print(df.duplicated())
#print(df[df.duplicated()])

#drop_duplicates -> 중복 제거
#df_unique = df.drop_duplicates()
#print(len(df), len(df_unique))
#print(df_unique.duplicated().sum())

#subset으로 기존 컬럼 셋팅
#df_u = df.drop_duplicates(subset=["machine_id", "cycle"], keep="last")
#print(len(df_u)

#reset_index -> 중복 제거 후 끊긴 인덱스를 다시 부터 매김
#df_clean = df.drop_duplicates().reset_index(drop=True)
#print(df_clean.index)

print('-' * 20)
Q1 = df["사이클타임"].quantile(0.25)
Q2 = df["사이클타임"].quantile(0.5)
Q3 = df["사이클타임"].quantile(0.75)
IQR = Q3 - Q1
min = Q1 - (1.5 * IQR)
max = Q3 + (1.5 * IQR)
print("IQR", round(IQR,2), "상한", round(max,2), "하한", round(min,2))

print('-' * 20)
time_error = df.loc[(df['사이클타임'] < min) | (df['사이클타임'] > max), '사이클타임']
print(time_error)
print("합계:", time_error.sum())
print("평균:", round(time_error.mean(), 2)) #자료를 그래로 가져와서 sum, mean이 50, 60, 70등 자료 값으로 계산됨

mask = (df['사이클타임'] < min) | (df['사이클타임'] > max)
print(df[mask][['샷', '사이클타임', '상태']])
print("합계", mask.sum())
print("비율", round(mask.mean(),2 )) #mask series로 True, False 0 1로 판단함, 값이 1이기 때문에 sum은 갯수 mean은 비율이 됨

print('-' * 20)
#박스플롯으로 이상치 확인
#import matplotlib.pyplot as plt
#df['사이클타임'].plot(kind='box')
#plt.savefig('cycle_box.png'); plt.close()

print('-' * 20)
good = df[~mask]
print(len(df), len(good))
print(round(good['사이클타임'].mean(), 2))