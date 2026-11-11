import pandas as pd
import numpy as np

#조건 = df['비스킷두께'] >= 16
#print(조건.head(3).tolist())
# [False, False, False]
#print(조건.sum())      # 74  (참의 개수)
#print(len(조건))       # 200 (전체 행 수)

PATH = 'data/13_diecasting_shot.csv'
df = pd.read_csv(PATH)
print(df.shape)
print('-' * 20)
num = df['비스킷두께'] >= 16
print(num.sum()) # 참의 개수
print(len(num)) # 전체 행 개수
low = df['비스킷두께'] < 16
print(low.sum()) # 거짓의 개수 => 참과 거짓을 더하면 200이 안된다(nan 때문에)

#(df['비스킷두께']>=16) & (df['사이클타임']>=25) -> 정상
# df['비스킷두께']>=16 & df['사이클타임']>=25 -> 오류
#both = df[(df['비스킷두께']>=16) & (df['사이클타임']>=25)]
#either = df[(df['비스킷두께']>=16) | (df['사이클타임']>=25)]
#print(len(both), len(either))   # 72 86
#df[~(df['품질등급'] == '불량')]는 불량이 아닌 행 
print('-' * 20)
both = df[(df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)]
print(len(both))
either = df[(df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)]
print(len(either))
error = df[(df['품질등급'] == '불량')]
print(len(error))
not_error = df[~(df['품질등급'] == '불량')]
print(len(not_error))

#df['품질등급'].isin(['주의', '불량']) 처럼 목록으로 전달
#str.countains : 해당 문자열을 포함하는 값
#df['설비ID'].str.contains('A') 로 A라인 전체 — 111행
#print(df['설비ID'].head(1).tolist())               # ['DIE-A-01']
#print(df['설비ID'].str.split('-').head(1).tolist())  # [['DIE', 'A', '01']]
#라인 = df['설비ID'].str.split('-').str[1]     # 가운데 조각만
#호기 = df['설비ID'].str.split('-').str[2]     # 마지막 조각만
#print((라인=='A').sum(), (라인=='B').sum(), (라인=='C').sum())   # 111 74 15
#print((호기=='01').sum(), (호기=='02').sum())                    # 114 86
#print(df['설비ID'].str.replace('DIE-', '', regex=False).head(1).tolist())
#['A-01']      앞머리를 걷어내 짧은 이름으로
print('-' * 20)
warn = df[(df['품질등급'] == '주의') | (df['품질등급'] == '불량')]
print(len(warn))
shot = df[(df['비스킷두께'] <= 16) & (df['비스킷두께'] >= 10)]
print(len(shot))
name = df['설비ID'].str.contains('A').sum()
print(name, 'A가 들어간 개수')
line = df['설비ID'].str.split('-').str[1]
num = df['설비ID'].str.split('-').str[2]
ho = (num == '01').sum()
nam = (line == 'A').sum()
cor = (num == '01') & (line == 'A') 
print(ho, "01이 들어간 개수")
print(cor.sum(), "전체 일치 개수")

#df.sort_values('비스킷두께') -> 비스킷두께 열 세움(내림차순)
#df.sort_values(['품질등급', '사이클타임'], ascending=[True, False])
#품질등급은 가나다순, 동률은 사이클타임 큰순
#df.sort_values('비스킷두께', ascending=False).head(5)   ==   df.nlargest(5, '비스킷두께')
#상위 몇개만 추출
print('-' * 20)
bisk = df.sort_values('비스킷두께', ascending = False)
print(bisk.head(5))
a = df.sort_values(['품질등급', '사이클타임'], ascending = [True, False])
print(a.head(5))

print('-' * 20)
#df[조건].copy() = 원본과 분리된 독립 복사본
#불량 = df[df['품질등급'] == '불량'].copy()
#불량['위험등급'] = '높음'          # 없는 이름에 대입 → 새 열
#print(불량.shape)                 # (20, 9)    열이 8에서 9로
#판정 = df.copy()
#판정['라인'] = 판정['설비ID'].str.split('-').str[1]   # 앞에서 만든 값을 열로
#판정.loc[판정['비스킷두께'] >= 16, '두께판정'] = '두꺼움'
#print(판정['두께판정'].notna().sum())    # 74     조건에 맞는 행만 채워짐
#판정['여유형체력'] = 판정['형체력'] - 250        # 열끼리·숫자와 계산도 가능
#print(판정['여유형체력'].head(3).tolist())       # [8.0, 7.0, 4.0]

df_copy = df[(df['품질등급'] !='양품') & (df['비스킷두께'] >= 16)].copy()
line = df_copy.sort_values('비스킷두께', ascending = False)
print(line.shape)
print(line.head(5))

#서로 다른 자료 2개 붙이기 
#import pandas as pd
#log = pd.read_csv('data/13_diecasting_shot.csv')
#master = pd.read_csv('data/13_diecasting_master.csv')
#three = log.head(3)[['샷', '설비ID', '비스킷두께']]   # 앞 세 줄 · 세 칸만
#print(three.to_string(index=False))
#  샷      설비ID  비스킷두께
#  1  DIE-A-01   10.0
#  2  DIE-B-01   11.0
#print(three.merge(master, on='설비ID').to_string(index=False))
#  샷      설비ID  비스킷두께 라인  도입연도  정격형체력 담당반
#  1  DIE-A-01   10.0  A   2018    280  1반
#  2  DIE-B-01   11.0  B   2020    320  2반

#print(log.shape, master.shape)          # (200, 8) (5, 5)
#merged = log.merge(master, on='설비ID')   # on = 두 표를 잇는 키 열
#print(merged.shape)                     # (185, 12)
# 열은 8 + 5 - 1 = 12   키 열 설비ID 는 한 번만 남는다
#print(merged[['샷', '설비ID', '라인', '도입연도']].head(2).to_string(index=False))
#  샷      설비ID 라인  도입연도
#  1  DIE-A-01   A   2018
#  2  DIE-B-01   B   2020
print('-' * 20)
master = pd.read_csv('data/13_diecasting_master.csv')
print(df.shape, master.shape)
print(df.columns) # 헤더 확인
print(master.columns) # 설비ID
merge = df.merge(master, on = '설비ID')
print(merge.shape)
print(merge.head(2))

#m_inner = log.merge(master, on='설비ID')                  # 기본 inner
#m_left  = log.merge(master, on='설비ID', how='left')
#m_outer = log.merge(master, on='설비ID', how='outer')
#print(m_inner.shape, m_left.shape, m_outer.shape)
# (185, 12) (200, 12) (201, 12)

#print(m_left['라인'].isna().sum())        # 15   짝을 못 찾아 빈 칸이 된 줄
#print(m_left[m_left['라인'].isna()]['설비ID'].head(1).tolist())
# ['DIE-C-01']    대장에 없는 설비
#print(m_outer[m_outer['샷'].isna()]['설비ID'].tolist())
# ['DIE-D-01']    로그에 없는 설비 — outer 로만 보인다

#unmatched = m_left[m_left['라인'].isna()] - 문제 항 찾기
#print(unmatched['설비ID'].head(1).tolist(), len(unmatched))
# ['DIE-C-01'] 15
print('-' * 20)
inner = df.merge(master, on = '설비ID')
left = df.merge(master, on = '설비ID', how = 'left')
outer = df.merge(master, on = '설비ID', how = 'outer')
print(inner.shape)
print(left.shape)
print(outer.shape)
less = left[left['라인'].isna()]
les = outer[outer['샷'].isna()]
print(less['설비ID'].head(1).tolist(), len(less))
print(les['설비ID'].head(1).tolist(), len(les))