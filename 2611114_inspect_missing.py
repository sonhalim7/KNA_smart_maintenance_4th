from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
PROC = DATA / '15_사출성형_공정.csv'
LOG = DATA / '15_사출성형_로그.csv'
df = pd.read_csv(PROC)
print(df.shape)  # (250, 22)

F_PROC = "data/15_사출성형_공정.csv"
F_LOG = "data/15_사출성형_로그.csv"

#NA_RULES = {
#'배럴온도': [999],
#'사출압력': [0],
#'스크루속도': [-999],
#}
#log_clean = pd.read_csv(LOG, na_values=NA_RULES)
#print(log_clean.isna().sum())
#print(log_clean['불량여부'].equals(log_raw['불량여부']))  # True

df = pd.read_csv(F_LOG)
df_a = pd.read_csv(F_PROC)
print(df.isna().sum())

df_c = pd.read_csv(F_LOG, na_values = {'배럴온도': [999], '스크루속도': [-999]})
print(df_c.isna().sum())

df_d = pd.read_csv(F_LOG, na_values = {'배럴온도': [999], '스크루속도': [-999], '사출압력': [0]})
print(df_d.isna().sum())

#count = df.isna().sum()
#ratio_pct = count / len(df) * 100
#print(count[count > 0])
#print(ratio_pct[ratio_pct > 0].round(1))
#print(int(count.sum()))       # 475
print('-' * 20)
count = df_a.isna().sum()
per = count / len(df_a) * 100
print(per)
miss = pd.DataFrame({'개수': count, '비율': per}) #DataFrame 개수, 비율로 이루어진 2열 표를 생성한다.
miss = miss[miss['개수'] > 0] #결측이 있는 열만 고르기
print(miss)

count = df_a.isna().sum()
ratio_pct = count / len(df) * 100
summary = pd.DataFrame({'결측개수': count, '결측률': ratio_pct})
missing_summary = summary.loc[summary['결측개수'] > 0].copy()
print(len(missing_summary))
#print(df.isna().sum().head())  # 기본axis=0: 열마다합계
#row_missing = df.isna().sum(axis=1)
#print(row_missing.head())      # axis=1: 한행안에서합계
#print(int((row_missing == 0).sum()))   # 76
#print(int((row_missing > 0).sum()))    # 174

print('-' * 20)
count = df_a.isna().sum()
per = count / len(df_a) * 100
num_per = per.sort_values(ascending = False) # 결측률 내림차순으로 정렬
print(num_per.head(3)) #결측률 상위 3개 출력

na_count = df_a.isna().sum(axis = 1) #axis = 0 열기준, axis = 1 행기준
na_real = df_a[na_count > 0]
not_na = df_a[na_count == 0]
print("결측 있는 행: ", len(na_real))
print("결측 없는 행: ", len(not_na))
lot_na = df_a[na_count >=  5]
print("결측이 5개 이상: ", len(lot_na))

print('-' * 20)
two_nan = df_a[['최대사출속도', '감압시간']].isna()
print(two_nan.sum())
print(two_nan.head(10))
nan_eq = df_a['최대사출속도'].isna() & df_a['감압시간'].isna()
print("동시 결측 행 수: ",nan_eq.sum())
print("비율: ",nan_eq.sum()/len(df_a) * 100)
print(df_a[nan_eq][['측정시각', '사출기']])
one_nan = df_a['측정시각'].isna() ^ df_a['사출기'].isna() # ^ xor 하나만 빈걸 찾는다 |는 두개 다 빈거 포함
print("한 열만 결측",one_nan.sum())
both_nan = df_a['최대사출속도'].notna() & df_a['감압시간'].notna() # 결측이 아닌 관측이기 때문에 notna 사용
print("두 열 모두 관측", both_nan.sum())
both_nan = df_a['측정시각'].notna() & df_a['사출기'].notna()
print(both_nan.sum()) # 두열 모두 관측 141개, 모두 결측 109개로 총 250개

print('-' * 20)
count_na = df_a.isna().sum()
exist_na = count_na[count_na > 0] # 결측 있는 열만 남기기
na_rate = round((exist_na / len(df_a)) * 100, 2)
line_rate = na_rate.sort_values(ascending = False)
print(line_rate)