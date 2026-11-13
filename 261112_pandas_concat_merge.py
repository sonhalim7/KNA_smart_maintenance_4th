import pandas as pd
import numpy as np

# ① 같은 표를 모은다 — concat
#year = pd.concat([part1, part2], ignore_index=True)
#print(year.shape)                      # (200, 8)   칸 수 그대로, 줄만 더해짐
# ② 정보를 더한다 — merge
#report = year.merge(master, on='설비ID', how='left')
#print(report.shape)                    # (200, 12)  줄 수 그대로, 칸만 더해짐
#print(report['라인'].isna().sum())      # 15   붙지 않은 줄은 여기서 드러난다
# concat 뒤에는 칸 수를, merge 뒤에는 줄 수를 본다

#iloc 번호 기준으로 찾는다. loc 위치를 찾는다.
PATH = 'data/13_diecasting_shot.csv'
R = 'data/13_diecasting_small.csv'
DATA = 'data/13_diecasting_master.csv'
df = pd.read_csv(PATH)
df_a = pd.read_csv(R)
df_b = pd.read_csv(DATA)
part1 = df.iloc[:100].reset_index(drop = True) #0~99까지 번호 순으로 찾는다.
part2 = df.iloc[100:].reset_index(drop = True) # 100~끝까지 번호순으로 찾는다.
stack = pd.concat([part1, part2]) #part1,2를 합친다.
print(stack.shape)
print(len(stack.loc[[0]])) #라벨이 0인 갯수 확인 loc[0] 열로 확인, loc[[0]] 행으로 확인
#drop = True로 첫 행을 0으로 만들어서 0이 두개가 되었다.
stacked = pd.concat([part1, part2], ignore_index = True)
print(stacked.index[-1])

print('-' * 20)
data = df.merge(df_a, how = 'left')
print(data.isna().sum())
data_a = data.dropna() # nan인 곳을 drop
print(data_a.shape) # 남은 줄 186(제목 포함) 데이터는 185줄
grade = data_a[data_a['품질등급'] != '양품']
grade_sort = grade.sort_values('비스킷두께', ascending = False)
grade_sort['라인'] = grade_sort['설비ID'].str.split('-').str[1] #'라인'이라는 list 제작
print(grade_sort[['샷', '라인', '설비ID', '비스킷두께', '품질등급']].head(5)) #이중 대괄호 사용해야한다.
