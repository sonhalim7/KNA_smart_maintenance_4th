import numpy as np

path = r"C:\Users\coco\Desktop\posco\data\11_hydraulic_cooler_20_261105_2.csv"
def hyd(i):
    return np.genfromtxt(path, delimiter = ',', skip_header = 1, usecols = i, encoding = 'utf-8')
cycle = hyd(0)
temp = hyd(1)
vib = hyd(2)
eff = hyd(3)
pow = hyd(4)
stat = hyd(5)

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

q1, q3 = np.percentile(temp, [25, 75])
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print(f"상한: {round(upper, 1)}, 걸리는 값: {temp[temp > upper]}, 걸리는 건: {len(temp[temp > upper])}건")

# z-score = (값 - 평균) / 표준편차 -> 단위가 다른 값들도 함께 비교할 수 있다.
#z = (vib - np.mean(vib)) / np.std(vib)
# 절댓값 2 초과 = 이상치
#print(vib[np.abs(z) > 2])
# 출력: [6.5]
temp_mid = np.mean(temp)
temp_std = np.std(temp)
z = (temp - temp_mid) / temp_std
print(f"최대 z 값{round(z.max(), 2)}, 자리{cycle[z>2]}") # python자리는 0부터 시작하니깐 +1을 해야 1번부터 시작하는 자리가 된다.
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

m = np.mean(temp)
s = np.std(temp)
upper = m + 3 * s #3시그마 상한
print(f"상한값: {round(upper, 2)}, 값 자리: {cycle[temp > upper]}") #[안에는 무조건 조건을 넣어 true나 false가 나오게 한다]

# 온도와 진동 두 센서
#temp = np.array([70, 72, 74, 76, 78])
#vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
# 상관행렬의 [0,1] 칸이 두 센서의 상관계수
#print(round(float(np.corrcoef(temp, vib)[0, 1]), 3))
# 출력: 0.998
#상관계수가 높으면 값이 같이 움직인다. 0.99 -> 하나가 오르면 같이 오름, -0.99 -> 하나가 오르면 하나는 떨어짐, 0.1 -> 관계없음

a = np.corrcoef(temp, eff)
print(round(a[0, 1], 2))
# => -0.99 대각선 아래로 간다. 한 값이 올라가면 다른 값은 떨어진다.


# 행은센서, 열은시점인2D 행렬
#data = np.array([[70., 72., 74.],
#[2.0, 2.2, 2.5]])
# axis=1 → 센서별평균(행방향)# axis = 0은 열방향
#print(np.round(np.mean(data, axis=1), 2))
# 출력: [72. 2.23]

data = np.array([temp,vib,eff, pow]) # =np.stack([temp, vib, eff, pow], axis = 0)
print(data.shape)
sensor_mean = np.round(np.nanmean(data, axis=1),1) # 결측값 중 nan이 포함되어있어서 nanmean을 써야한다
sensor_std = np.round(np.nanstd(data, axis =1),1)
print(f"센서별 평균: {sensor_mean}, 흩어진 정도: {sensor_std}")

# 앞은안정, 뒤는상승한진동데이터
#vib = np.array([2.0, 2.1, 2.0, 5.0, 5.2, 5.1])
# 평균뺀값의누적합
#cs = np.cumsum(vib -np.mean(vib))
# 가장낮은위치= 변화직전
#print(np.argmin(cs))
# 출력: 2

all_mean = np.nanmean(temp)
cs = np.cumsum(temp -all_mean)
low = np.argmin(cs)
print(low+1, low+2) #사람이 보는 번호로 표시 (python은 1번이 0부터 표시한다.)
#50개의 자료중 사람이 볼때 45, 46간격이 가장 크다면 파이썬에서는 해당 간격을 44번으로 본다. 따라서 45, 46번을 표시하려면 low+1, low+2

# 온도(1열)와 냉각효율(3열)로 2×50 배열 생성
#F = "data/11_hydraulic_cooler.csv"
#data = np.genfromtxt(F, delimiter=",", skip_header=1, usecols=(1, 3)).T
#m = np.nanmean(data, axis=1, keepdims=True) axis = 1 자료를 행으로 쌓는다.
#s = np.nanstd(data, axis=1, keepdims=True)
#score = np.abs((data - m) / s).sum(axis=0)
#print(np.argmax(score))      # 49 (0부터 세는 인덱스)
#print(np.argmax(score) + 1)  # 50 (사이클 번호

# z-score = (값-평균) / 표준편차 => 표준화!!
temp_mean = np.nanmean(temp)
temp_std = np.nanstd(temp)
temp_z = np.abs((temp - temp_mean) / temp_std) #온도 zscore 표준화

eff_mean = np.nanmean(eff)
eff_std = np.nanstd(eff)
eff_z = np.abs((eff-eff_mean)/eff_std) #효울 zscore 표준화
total_score = temp_z + eff_z
high_score = np.argmax(total_score)
high = round(np.max(total_score),2)
score = np.argsort(total_score)[::-1]
print(f"최고점수{high_score+1}, ({high}) 상위 세 시점 {score[0:3]+1} ")
#python은 번호가 0부터 시작

