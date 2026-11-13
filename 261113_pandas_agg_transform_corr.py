import numpy as np
import pandas as pd

#agg 방식
#print(df.groupby("냉각기상태")["온도"].agg(
# ["mean","std","max"]).round(2))
#     mean   std   max
# 고장54.67  3.76  57.8
# 저하45.46  1.47  51.2
# 정상35.89  0.36  36.4 
# 여러열을선택한뒤리스트방식을쓸수도있습니다.
# print(df.groupby("냉각기상태")[["온도","진동"]].agg(
# ["mean","std"]).round(3))

#agg 이름 붙이기 코드
# summary =df.groupby("냉각기상태").agg(
# 평균온도=("온도","mean"),
# 온도표준편차=("온도","std"),
# 평균진동=("진동","mean"),
# 유효온도수=("온도","count"),
#)
# print(summary.round(2))

# 정상지원: 열별로다른통계목록을지정 #대괄호 사용
# print(df.groupby("냉각기상태").agg({
# "온도":["mean","std"],
# "진동":["mean","max"]
# }).round(3))
 
# 결과열이름을직접정하려면named aggregation
# print(df.groupby("냉각기상태").agg(
# 평균온도=("온도","mean"),최대진동=("진동","max")
# ).round(3))

FILE = 'data/14_hydraulic_qc.csv'
df = pd.read_csv(FILE)
COUNT = df['검사결과'].value_counts()
print(COUNT)
deg = df.groupby("검사결과")['온도'].agg(['mean', 'std', 'max']).round(2)
print(deg)
check =df.groupby("검사결과").agg(평균온도 = ("온도", 'mean'), 
                              평균냉각효율 = ('냉각효율', 'mean'),
                                측정수 = ('온도', 'count')).round(2)
print(check)
# 평균 온도가 높고 냉각효율이 떨어진다.

print('-' * 20)
#transform = 그룹 통계를 원래 행에 붙인다.
# print(df.groupby("냉각기상태")["온도"].mean().shape) # (3,)
# print(df.groupby("냉각기상태")["온도"].transform("mean").shape)
# (120,)
# marked =df.copy()
# marked["그룹평균"]=marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"]=marked["온도"]-marked["그룹평균"]
# print(marked[["냉각기상태","온도","그룹평균","편차"]].head(3).round(2))
# 첫행: 고장/ 35.6 / 54.67 / -19.07
# print(marked.groupby("냉각기상태")["편차"].sum().round(10))
# 각그룹에서0 또는부동소수점정밀도수준의작은값

#pivot_table = 두 기준 테이블을 한번에 정렬
# temp_table =pd.pivot_table(
# df,index="밸브상태",columns="운전부하",values="온도",
# aggfunc="mean",margins=True,margins_name="전체"
# )
# print(temp_table.round(2))
#        고부하저부하전체
# 경미42.20   47.52  44.86
# 심각45.25   47.09  46.02
# 정상39.34   49.40  45.11
# 지연43.75   49.79  45.86
# 전체41.85   48.82  45.34

# print(pd.crosstab(df["냉각기상태"],df["운전부하"]))

PATH = 'data/14_hydraulic.csv'
df_a = pd.read_csv(PATH)
ice = df_a.copy()
ice['평균'] = df_a.groupby("냉각기상태")['온도'].transform("mean") #평균을 새열로 붙인다.
ice['편차'] = ice['온도'] - ice['평균'] #편차 추가
ice_group = ice.sort_values(by = '편차', key = abs, ascending = False) #편차를 절댓값 씌워서 정렬
print(ice_group.head(3))

print('-' * 20)
# corr 상관계수
# print(round(df["온도"].corr(df["진동"]),3)) # 0.931
# print(round(df["온도"].corr(df["압력"]),3)) # 0.284
# print(round(df["온도"].corr(df["냉각효율"]),3)) # -0.951
 
# 각짝의두값이모두존재하는행수를확인합니다.
# valid =df[["온도","냉각효율"]].dropna()
# print("유효한관측쌍:",len(valid)) # 120
 
# 잘못된예(실행하지않음): 비교할열자체가필요합니다.
# df["온도"].corr("진동")

df_vib = round(df['온도'].corr(df['진동']), 2)
print("온도, 진동:",df_vib)
df_pres = round(df['온도'].corr(df['압력']), 2)
print("온도, 압력:", df_pres)
df_eff = round(df['온도'].corr(df['냉각효율']), 2)
print("온도, 냉각효율:", df_eff)
df_all = round(df[['온도', '압력', '냉각효율', '진동']].corr(), 2)
print(df_all)

print('-' * 20)
qc = pd.read_csv('data/14_hydraulic_qc.csv')
sensor_cols =qc.select_dtypes(include="number").columns.tolist() #qc는 파일을 읽는거
corr_matrix =qc[sensor_cols].corr()
rows =[]
# i보다뒤에있는열j만선택→ 자기자신과대칭중복제외
for i in range(len(sensor_cols)):
  for j in range(i +1,len(sensor_cols)):
    a =sensor_cols[i]
    b =sensor_cols[j]
    rows.append({"지표1":a,"지표2":b,
            "상관계수":corr_matrix.loc[a,b]}) #상관계수를 표로 만들기
pair_table =pd.DataFrame(rows)
pair_table["절댓값"]=pair_table["상관계수"].abs() #part table에 절댓값 추가
print(corr_matrix.shape,len(pair_table)) # (10, 10) 45
print(pair_table.head(3).round(3))
count_4 = (pair_table["절댓값"] >= 0.4).sum()
count_5 = (pair_table["절댓값"] >= 0.95).sum()

print(f"절댓값 0.4 이상: {count_4}개")
print(f"절댓값 0.95 이상: {count_5}개")

top5 = (
    pair_table[pair_table["절댓값"] >= 0.95]
    .sort_values(by="절댓값", ascending=False)
    .head(5)
)
print(top5[["지표1", "지표2", "상관계수"]].round(4))

print('-' * 20)
df_b = pd.read_csv('data/14_hydraulic_std.csv')
data = df_a.merge(df_b, how = 'left')
print(data.shape)
data['온도구간'] =pd.cut(#구간화 cut
data["온도"],bins=[0,40,50,200],
labels=["낮음","보통","높음"],right=True)
print(data['온도구간'].value_counts(sort=False))

summary = data.groupby("냉각기상태").agg(측정수 = ("온도", "count"),
                                    평균온도 = ("온도", "mean"),
                                    온도표준편차 = ('온도', "std"),
                                    평균냉각효율 = ('냉각효율', 'mean'),
                                    위험도 = ("위험도", "first"),
                                    점검주기 = ("권장점검주기", "first")) 
#first를 써야 자료에 있는 숫자를 그대로 쓸 수 있다고함
print(summary)

print(pd.crosstab(data["온도구간"],data["냉각기상태"])) #열이 앞으로 오게
#crosstab 앞 열 뒤가 행인 표를 만든다. 더 자세하게 만들려면 pivot_table 사용
df_press = round(data['온도'].corr(data['냉각효율']), 2)
print(df_press)
df_vib = round(data['온도'].corr(data['진동']), 2)
print(df_vib)

num = summary.sort_values(by=['위험도', '평균온도'], ascending=[False, False]) # 내림차순
print(num)
