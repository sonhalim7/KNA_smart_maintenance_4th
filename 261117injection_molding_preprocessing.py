from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'
df = pd.read_csv(PROC)
# 원본df를덮어쓰지않습니다.
work = df.copy()

#실습 4
version = {'원본' : df, "행제거": df.dropna(), "thresh20" :df.dropna(thresh=20)}
comparison_rows = []

for name, frame in version.items():
    comparison_rows.append({
        '방식': name, '행 수': len(frame), 
        '손실률_%': (1-len(frame) / len(df)) * 100,
        '불량수': int(frame['불량여부'].sum()),
        '불량비율_%': frame['불량여부'].mean() * 100
    })
comparison = pd.DataFrame(comparison_rows)
print(comparison.round(1).to_string(index = False))

df_drop = df.dropna()
df_thr = df.dropna(thresh = 20)
print("행 수", len(df_drop), len(df_thr))
print("drop 손실률", 100 - len(df_drop)/len(df) * 100, "%") # 계산은 전체 대비 drop의 비율이므로 100%에서 drop 비율을 빼야 손실율이 나온다.
print("thresh 20 손실률", 100 -len(df_thr)/len(df) * 100, "%")

df_drop_count = (df_drop['불량여부'] == 1).sum()
df_thr_count = (df_thr['불량여부'] == 1).sum()
print("drop불량비율", round(df_drop_count/len(df_drop) * 100, 2),"%")
print("thresh불량비율", round(df_thr_count / len(df_thr) * 100, 2),"%")

print('-' * 20)
mask = df['최대사출압'].isna()
mean_value = df['최대사출압'].mean()
median_value = df['최대사출압'].median()
mean_fill = df['최대사출압'].fillna(mean_value)
median_fill = df['최대사출압'].fillna(median_value)
mean_fill_nan = mean_fill.isna().sum()
median_fill_nan = median_fill.isna().sum()
print(mask.sum(), mean_fill_nan, median_fill_nan)
print(mask.head(3))
print(mean_fill.head(3))
print(median_fill.head(3))

print('-' * 20)
#grade = pd.Series(['L', 'L', None, 'M', 'H', 'L'], dtype='string')
#modes = grade.mode()
#print(modes.tolist())              # ['L']
#mode_filled = grade.fillna(modes.iloc[0])
#print(mode_filled.tolist())
#print(pd.Series(['A', 'B', None]).mode().tolist()) # ['A', 'B'] #최빈값 구하기

series_demo = pd.Series([None, 73.0, None, None, 75.0])
print(series_demo.ffill().tolist()) #ffill 앞에서 마지막으로 확인한 값으로 채움
# [NaN, 73, 73, 73, 75]
print(series_demo.ffill(limit=1).tolist()) #limit 연속 결측 구간에서 최대 몇칸을 채울지
# [NaN, 73, 73, NaN, 75]
print(series_demo.bfill().tolist()) #bifill 뒤에서 처음 확인되는 값으로 채움
# [73, 73, 75, 75, 75] 

F_PROC = "data/15_사출성형_공정.csv"
F_LOG = "data/15_사출성형_로그.csv"
print('-' * 20)
NA_RULES = {'배럴온도': [999], '사출압력' : [0], '스크루속도': [-999]}
log = pd.read_csv(F_LOG, na_values = NA_RULES, parse_dates =['측정시각']) #측정시각을 날짜, 시간으로 변환
log['측정시각'] = pd.to_datetime(log['측정시각'], errors='raise') #날짜, 시간변환 명시적 확인(에러처리)
unknown = log.loc[log['사출기'].isna()].copy()
known = log.loc[log['사출기'].notna()].copy()

known = known.sort_values(['사출기', '측정시각'])
print(len(known), len(unknown)) #15, 1
print(int(log.isna().sum().sum())) 

#앞의 값
candidate =(known.groupby('사출기')['배럴온도'].ffill(limit = 1))

#온도가 실제로 있었던 시각만 표시
observed_at = known['측정시각'].where(known['배럴온도'].notna())
last_time = observed_at.groupby(known['사출기']).ffill()
gap = known['측정시각'] - last_time
can_fill = (known['배럴온도'].isna() & candidate.notna()
            & gap.le(pd.Timedelta('2min')))

#gap.le(pd.Timedelta('2min'))
#-le : 이하인지 비교
#-ge : 이상인지 비교
# -pd.Timedelta('2min') : 2분

# 허용 위치에 온도넣기
known.loc[can_fill, "배럴온도"] = candidate.loc[can_fill]
print(int(can_fill.sum()))