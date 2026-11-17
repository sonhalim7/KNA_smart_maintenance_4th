from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent
PROC = ROOT / 'data' / '15_사출성형_공정.csv'
df = pd.read_csv(PROC)
# 원본df를덮어쓰지않습니다.
work = df.copy()

#dropna는 결측이 있는 행또는 열을 선택한 기준으로 제거

rows_removed = df.dropna()         # 기본axis=0: 행제거
cols_removed = df.dropna(axis=1)   # axis=1: 열제거
print(rows_removed.shape)          # (76, 22)
print(cols_removed.shape)          # (250, 10)
print(df.shape)                    # 원본은(250, 22)
print(df.dropna(how='any').shape)  # (76, 22)
print(df.dropna(how='all').shape)  # (250, 22)
# 모든 측정입력이 빈행만 확인하려면 검사범위를 좁힙니다.
#print(df.dropna(how='all', subset=feature_cols).shape)

print(df.dropna(thresh=20).shape)   # (162, 22)
# 수치형공정변수19열에서결측을최대2개허용
#min_valid = len(feature_cols) -2
#print(min_valid)                   # 17
#print(df.dropna(subset=feature_cols, thresh=min_valid).shape)

#subset: 중요한 열만 검사 (해당 열 결측 검사)
print('-' * 20)
print(df.shape)
print(df.dropna().shape) #결측 행 제거
print(df.dropna(axis = 1).shape) #결측 열 제거
print('-' * 20)
print(df.dropna(how = 'all').shape) #all은 모두 비여있어야 삭제, any는 하나라도 비어있으면 삭제
print(df.dropna(thresh = 20).shape) #최소겟수 20개로 제한 행이 20개보다 적으면 삭제
count = df.dropna(subset = '불량여부')
print(count.shape)

print('-' * 20)
count_na = df.isna().sum()
na_rate = round((count_na / len(df)) * 100, 2)
print(na_rate)
high_per = na_rate[na_rate >= 40].index.tolist() # 열 이름 목록으로 남기기
print(high_per)
df_drop = df.drop(columns = high_per) #drop으로 40%가 넘는 열 제거
print("열크기", df_drop.shape)
print("열 이름", df_drop.columns.tolist())

print('-' * 20)
df_drop = df.dropna()
df_thr = df.dropna(thresh = 20)
print("행 수", len(df_drop), len(df_thr))
print("drop 손실률", 100 - len(df_drop)/len(df) * 100, "%") # 계산은 전체 대비 drop의 비율이므로 100%에서 drop 비율을 빼야 손실율이 나온다.
print("thresh 20 손실률", 100 -len(df_thr)/len(df) * 100, "%")

df_drop_count = (df_drop['불량여부'] == 1).sum()
df_thr_count = (df_thr['불량여부'] == 1).sum()
print("drop불량비율", round(df_drop_count/len(df_drop) * 100, 2),"%")
print("thresh불량비율", round(df_thr_count / len(df_thr) * 100, 2),"%")