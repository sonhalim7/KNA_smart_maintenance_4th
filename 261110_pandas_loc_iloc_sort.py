import pandas as pd
import numpy as np

df = pd.read_csv('data/13_diecasting_small.csv')
hy = df['형체력']
print(hy.head(3))
# 0    258.0
# 1    257.0
# 2    253.0
# Name: 형체력, dtype: float64
print(df[['형체력', '실린더압력']].shape)
print(df[['형체력', '실린더압력']].dtypes)
print(df[['형체력']].dtypes)

#정렬 = df.sort_values('형체력', ascending=False)
#print(정렬.index[:4].tolist())        # [22, 17, 27, 12]   이름표가 뒤죽박죽
#재번호 = 정렬.reset_index(drop=True)
#print(재번호.index[:4].tolist())      # [0, 1, 2, 3]
#print(재번호.loc[0, '샷'], 재번호.iloc[0]['샷'])   # 23 23   다시 같아짐
# drop=True 를 빼면 옛 이름표가 index 라는 열로 남는다
#print(정렬.reset_index().shape)       # (30, 9)   열이 하나 늘어남

print(df[['형체력', '실린더압력']])
#라벨 - 그 행에 붙은 이름표, 인덱스 값
#위치번호 - 맨위에서부터 몇 번째인지, 항상 0부터
sorted = df.sort_values('형체력', ascending = False) # 내림차순, True = 오름차순
print("정렬 후 인덱스 값 4개:", sorted.index[:4].tolist()) #tolist() list로 변환
print("정렬 후 iloc[#] 샷:", int(sorted.iloc[0]['샷'])) #눈에 보이는 순서
print("정렬 후 loc[#] 샷:", int(sorted.loc[0,'샷'])) #원래 순서

print(df.loc[0:4].shape) #[5.8]
print(df.iloc[0:4].shape) #[4.8]

print(df.loc[0:4, ['실린더압력', '형체력']].shape) # 5,2
print(df.iloc[0:5, [2,6]].shape)

print(int(df.loc[0, '샷']))
print(int(df.iloc[0]['샷']))
sorted_values = df.sort_values('형체력', ascending = False)
print(int(sorted_values.loc[0, '샷']))
print(int(sorted_values.iloc[0]['샷']))

print('-' * 20)
print(df.columns.tolist())
print(df.loc[0:4, ['실린더압력', '형체력']].shape) #loc는 맨 끝을 포함한다. 0:4 -> 5개
print(df.iloc[0:5, [2, 6]].shape) #iloc는 맨 끝 포함 x -> 0:5 -> 4개 [2,6] 3번째 7번째 실린더, 형체

df_a = pd.read_csv('data/13_diecasting_shot.csv')
print(df_a.shape)
print('-' * 20)
print(df_a.columns.tolist())
print('-' * 20)
print(df_a[['설비ID', '비스킷두께','품질등급']].head(10))
print(df_a.tail(5))
