import numpy as np
path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv" #r을 붙여야 \를 문자로 인식하지 않는다
def get_colum(i):
    return np.genfromtxt(path, delimiter = ',', skip_header = 1, usecols = i, encoding= 'utf-8')
name = get_colum(0)
cycle = get_colum(1)
ceil = get_colum(2)
pressure = get_colum(3)
shape = get_colum(4)

a = cycle.argmax()
print(cycle[a]) # 코딩에서 번호는 0부터 시작하기 때문에 사람이 읽는 번호로 표시하기 위해서는 코드 번호 +1을 해줘야한다
print(f"번호 {a+1}, 값 {cycle[a]}")

#np.sort(뭐시기) -> 뭐시기를 오름차순으로 정렬한다.

b = np.abs(np.diff(cycle)) #-> 절댓값을 씌우고 정렬해야 변화량을 구할 수 있다.
j = np.argmax(b)
print(f"값이 가장 크게 변화한 자리: {j+1}, {j+2}, 변화값: {cycle[j]}") #만약 49번째 차가 가장 크다면(49, 50자리) j는 48이된다 따라서 49, 50을 표현하려면 j+1, j+2로 각각 표시해야한다.

ceil[0] = 9999
print(ceil.mean())
fixed = np.clip(ceil, 100, 300) # 최솟값 100, 최댓값 300으로 조정
print(fixed.mean(), ceil.mean())

jam = 0
warn = 0
good = 0
for i in cycle:
    if i >= 1000:
        jam += 1
    elif i >= 50 and i < 1000:
        warn += 1
    else:
        good +=1

print(f"잼 = {jam}개, 경고 = {warn}개, 양호 = {good}개")
print("비율 = ", jam / 50, warn / 50, good / 50)

# 결측이 섞인 온도 센서 배열
#temp = np.array([70.1, np.nan, 71.2, np.nan])
# 결측 위치 (True가 nan 자리)
#print(np.isnan(temp))
# 출력: [False True False True]
# 결측 개수
#print(np.isnan(temp).sum())
# 2개

#np.nanmean· np.nanstd— 결측을건너뛰는통계함수

data_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_hydraulic_cooler.csv"
def data_hyd(i):
    return np.genfromtxt(data_path, delimiter = ',', skip_header = 1, usecols = i, encoding = 'utf-8')
hyd_cycle = data_hyd(0)
hyd_temp = data_hyd(1)
hyd_vib = data_hyd(2)
hyd_eff = data_hyd(3)
hyd_cool = data_hyd(4)
hyd_stat = data_hyd(5)

#실습 1
print(f"빈 자료 갯수{np.isnan(hyd_vib).sum()}")
a = np.isnan(hyd_vib).sum()
b = len(hyd_vib)
print(f"비율: {round(a/b, 2)}")
print(f"빈 값 제외한 평균: {round(np.nanmean(hyd_vib), 2)}")
print(f"빈 값 제외하지 않은 일반 평균: {np.mean(hyd_vib)}")


# 진동 센서 6개 시점
#vib = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
# 1사분위 (Q1) -25%
#print(round(float(np.percentile(vib, 25)), 2))
# 출력: 2.28
# 3사분위 (Q3) -> 75%
#print(round(float(np.percentile(vib, 75)), 2))
# 출력 = 2.95

#*****IQR***** -> 가운데 절반이 놓인 폭을 재고, 그1.5배까지를 정상 울타리로 삼음
# Q1, Q3를 한 번에 구하기
#q1, q3 = np.percentile(vib, [25, 75])
#iqr = q3 - q1
# 상한 경계
#upper = q3 + 1.5 * iqr
# 상한 초과 값만 골라내기
#print(vib[vib > upper])
# 출력: [6.5]

q1, q3 = np.percentile(hyd_temp, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print(f"상한: {round(upper, 1)}, 걸리는 값: {hyd_temp[hyd_temp > upper]}, 걸리는 건: {len(hyd_temp[hyd_temp > upper])}건")

# z-score = (값 - 평균) / 표준편차 -> 단위가 다른 값들도 함께 비교할 수 있다.
#z = (vib - np.mean(vib)) / np.std(vib)
# 절댓값 2 초과 = 이상치
#print(vib[np.abs(z) > 2])
# 출력: [6.5]
temp_mid = np.mean(hyd_temp)
temp_std = np.std(hyd_temp)
z = (hyd_temp - temp_mid) / temp_std
print(f"최대 z 값{round(z.max(), 2)}, 자리{hyd_cycle[z>2]}") # python자리는 0부터 시작하니깐 +1을 해야 1번부터 시작하는 자리가 된다.
#np.where = 튜플 값 -> +1을 하려면 [0]으로 값을 숫자로 꺼내야한다.

#시그마 규칙
# 평균과 표준편차
#m, s = np.mean(vib), np.std(vib)
# 3시그마 상한
#upper = m + 3 * s => zscore가 3인거랑 같다.
# 상한을 넘는 값 찾기
#print(vib[vib > upper])
# 출력: []
#작은 데이터는 3시그마로 느슨하게 잡고 중요한 데이터는 2시그마로 엄격하게 잡는 방식

m = np.mean(hyd_temp)
s = np.std(hyd_temp)
upper = m + 3 * s #3시그마 상한
print(f"상한값: {round(upper, 2)}, 값 자리: {hyd_cycle[hyd_temp > upper]}") #[안에는 무조건 조건을 넣어 true나 false가 나오게 한다]

# 온도와 진동 두 센서
#temp = np.array([70, 72, 74, 76, 78])
#vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
# 상관행렬의 [0,1] 칸이 두 센서의 상관계수
#print(round(float(np.corrcoef(temp, vib)[0, 1]), 3))
# 출력: 0.998
#상관계수가 높으면 값이 같이 움직인다. 0.99 -> 하나가 오르면 같이 오름, -0.99 -> 하나가 오르면 하나는 떨어짐, 0.1 -> 관계없음

a = np.corrcoef(hyd_temp, hyd_eff)
print(float(a[0, 1], 2))
# => -0.99 대각선 아래로 간다. 한 값이 올라가면 다른 값은 떨어진다.

