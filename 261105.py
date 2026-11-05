import os
import numpy as np

file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\10_mct_tool.csv"
 
with open(file_path, "r", encoding="utf-8") as f:
  header = f.readline().strip().split(",")

rpm_idx = -1
for idx, col in enumerate(header):
  if "회전수" in col or "rpm" in col.lower():
    rpm_idx = idx
    break
#데이터 오류
data = np.genfromtxt(
    file_path,
    delimiter=",",
    skip_header=1,
    usecols=rpm_idx,
    encoding="utf-8",
    filling_values=np.nan,
)


mean_val = np.mean(data)
std_val = np.std(data, ddof=1)
min_val = np.min(data)
max_val = np.max(data)

print(f"회전수 평균: {mean_val:.1f}")
print(f"표준편차: {std_val:.1f}")
print(f"최소: {min_val:.1f}")
print(f"최대: {max_val:.1f}")




file_path = (r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\10_mct_tool.csv")

with open(file_path, "r", encoding="utf-8") as f:
  header = f.readline().strip().split(",")

torque_idx = -1
for idx, col in enumerate(header):
  if "토크" in col or "torque" in col.lower():
    torque_idx = idx
    break

data = np.genfromtxt(
    file_path,
    delimiter=",",
    skip_header=1,
    usecols=torque_idx,
    encoding="utf-8",
    filling_values=np.nan,
)

overall_mean = np.mean(data)

filtered_data = data[data > 10]

count_val = len(filtered_data)
mean_filtered = np.mean(filtered_data)
diff = mean_filtered - overall_mean

print(f"골라낸 값들: {filtered_data}")
print(f"골라낸 값 개수: {count_val}개")
print(f"골라낸 값들의 평균: {mean_filtered:.1f}")
print(f"전체 평균: {overall_mean:.1f}")
print(f"전체 평균과의 차이: {diff:+.1f}")


file_path = (r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\10_mct_tool.csv")

with open(file_path, "r", encoding="utf-8") as f:
  header = f.readline().strip().split(",")

rpm_idx = -1
torque_idx = -1
for idx, col in enumerate(header):
  if "회전수" in col or "rpm" in col.lower():
    rpm_idx = idx
  if "토크" in col or "torque" in col.lower():
    torque_idx = idx

if rpm_idx == -1 or torque_idx == -1:
  raise ValueError("회전수 또는 토크 열을 찾을 수 없습니다.")

data = np.genfromtxt(
    file_path,
    delimiter=",",
    skip_header=1,
    usecols=[rpm_idx, torque_idx],
    encoding="utf-8",
    filling_values=np.nan,
)

print(f"구조: {data.shape}, 데이터 타입: {data.dtype}")

rpm_col_pos = 0 if rpm_idx < torque_idx else 1
rpm_data = data[:, rpm_col_pos]

overall_mean = np.mean(rpm_data)

low_rpm = rpm_data[rpm_data < 2000]

count_val = len(low_rpm)
mean_low = np.mean(low_rpm)

print(f"이상 시점: {count_val}개")
print(f"이상 평균: {mean_low:.1f}")
print(f"전체 평균: {overall_mean:.1f}")

tok = np.array([123, 124, 513, 53, 12, 8, 1241, 2130])
rotate = np.array([1234, 3454, 5632, 4522, 56, 3432, 6632, 32413])
data = np.array([[4603, 2], [4603, 21]])
check_rotate = rotate < 2000
print(rotate[check_rotate])
print(rotate[check_rotate], tok[tok > 250])
print(np.sum(check_rotate))
print(np.sum((rotate < 2000) | (tok > 250)))
print(np.mean(check_rotate) * 100)
print(np.mean((rotate < 200) | (tok > 250)) * 100)

check_tok = tok > 100
print(check_tok.sum())
print(round(check_tok.mean(), 2))

#  import numpy as np
#F = 'data/11_diecasting_series.csv'
#ct = np.genfromtxt(F,
# delimiter=',', # 값을 나누는 기호
# skip_header=1, # 첫 줄(제목)은 건너뜀
# usecols=1) # 2번째 열 = 사이클타임
# print(ct.shape, ct.dtype)
# 출력: (50,) float64
# 열 번호는 0부터
# 시점 0 · 사이클타임 1 · 실린더압력 2 · 주조압력 3 · 형체력 4

#import numpy as np
#vib = np.array([2.1, 6.1, 2.0, 5.8])
#print(np.sort(vib)) -> sort 값을 오름차순으로 배치
# 출력: [2. 2.1 5.8 6.1]
#print(np.argsort(vib)) -> 각 값의 원래 자리 표시
# 출력: [2 0 3 1]

#import numpy as np
#cycle = np.array([1, 2, 3, 4, 5])
#vib = np.array([2.1, 2.3, 6.1, 2.0, 5.8])
#pos = np.argmax(vib) -> 최대값이 위치하는 자리 [2]
#print(cycle[pos]) = print(cycle[2]) => 3이 된다.
# 출력: 3 

file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv"
cycle = np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = 1, encoding = 'utf-8')
time = np.genfromtxt(file_path, delimiter =',', skip_header = 0, usecols = 0, encoding = 'utf-8')
idx = cycle.argmax()
print(cycle[idx], time[idx])

#파일 탐색기에서 해당 파일에 대고 Shift + 우클릭을 한 뒤 [파일 경로로 복사]를 누르면 가장 정확한 경로를 가져올 수 있습니다.
#"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_hydraulic_cooler.csv"

#import numpy as np
#vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
#change = np.diff(vib) = 값의 차이 [0.1, 0.1, 4.8, 0.10]
#print(np.round(change, 1)) - round(a, 1) a를 소숫점 1자리로 표시
# 출력: [0.1 0.1 4.8 0.1]
#print(np.argmax(change)) argmax - 가장 크게 바뀐 것의 위치
# 출력: 2

#np.round - 소숫점 반올림, np.abs 절댓값
file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv"
time = np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = 0, encoding = 'utf-8')
cycle = np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = 1, encoding = 'utf-8')
change = np.diff(cycle)
a = np.abs(change)
max = np.argmax(a)
print(cycle[max], cycle[max+1], np.max(a))

#import numpy as np
#pres = np.array([4.5, 9999.0, 4.6, -1.0])
#fixed = np.clip(pres, 0, 10) -> 범위 초과 값을 범위로 끌어당김 9999->10으로 -1 -> 0으로
#print(fixed)

file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv"
cyl = np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = 2, encoding = 'utf-8')
cyl[0] = 9999
mid = cyl.mean()
print(round(mid, 1))
fixed = np.clip(cyl, 100, 300)
print(fixed.mean())


#import numpy as np
#defects = np.array([0, 1, 0, 2, 3, 5])
#print(np.cumsum(defects)) -> 값 차이의 누적
# 출력: [0 1 1 3 6 11]

#import numpy as np
#vib = np.array([2.1, 3.5, 2.0, 6.2])
#label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0)) -> 값이 5이상이면 2, 5보다 작으면 다시 조건 확인 -> 3보다 크면 1, 아니면 0
#print(label)
# 출력: [0 1 0 2]

#import numpy as np
#status = np.array([0, 0, 1, 0, 2, 1, 0])
#kinds, counts = np.unique(status, return_counts=True)
#print(kinds) -> 등장하는 숫자 0, 1, 2
#print(counts) -> 숫자 등장하는 횟수
# 출력: [0 1 2] / [4 2 1] -> 0이 4번, 1이 2번, 2가 1번 나왔다.

file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv"
cycle = np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = 1, encoding = 'utf-8')
jam = 0
warn = 0
ok = 0
for i in cycle:
  if i >= 1000:
    jam += 1
  elif i < 1000 and i >= 50:
    warn += 1
  else:
    ok += 1

per_jam = jam / len(cycle)
per_warn = warn / len(cycle)
per_ok = ok / len(cycle)
print(f"정상: {ok, per_ok}, 경고 {warn, per_warn}, 잼 {jam, per_jam}")

#import numpy as np
#vib = np.array([2.1, 2.3, 6.2, 2.0])
#print(np.any(vib > 5)) -> 하나라도 만족
# 출력: True
#print(np.all(vib < 10)) -> 모두 만족해야한다
# 출력: True

#import numpy as np
#am = np.array([2.0, 2.1, 2.2])
#pm = np.array([2.3, 2.4, 2.5])
#print(np.concatenate([am, pm])) -> 한줄로 쌓인다
# 출력: [2. 2.1 2.2 2.3 2.4 2.5]
#print(np.stack([am, pm]).shape) -> 밑으로 쌓인다. 2행 3열이 됨
# 출력: (2, 3)

import numpy as np
file_path = r"C:\Users\Admin\OneDrive - 서울과학기술대학교\바탕 화면\posco\data\11_diecasting_series.csv"
def get_colum(i):
  return np.genfromtxt(file_path, delimiter = ',', skip_header = 1, usecols = i, encoding = 'utf-8')
cycle = get_colum(1)
ceil = get_colum(2)
press = get_colum(3)
shape = get_colum(4)

stack = np.stack([cycle, ceil, press, shape])
print(stack.shape)
recent = stack[:, -10:] # 마지막 열 10개만 출력 -> -10은 없거나 한 개만 출력 -10:은 열 10개를 출력
print(recent.shape)

time = get_colum(0)
print(cycle.argmax()+1, cycle.max())
change = np.abs(np.diff(cycle)) #절댓값 씌워서 변화값 젤 큰거 찾기
print(change.argmax()+1, change.argmax()+2, change.argmax())
warn = (cycle >= 50) | (ceil < 150)
warn_per = (np.sum(warn) / len(cycle)) * 100
print(warn_per,"%")

# argsort()는 값이 작은 순서대로 인덱스를 정렬하므로, [::-1]로 뒤집어 큰 순서로 만듭니다.
#enumerate를 써서 함수 값과 순서를 함께 호출하기
top = np.argsort(cycle)[::-1] # 순서 뒤집기
top3 = top[:3] # 상위 3개 np.argsort(cycle)[::-1]을 안하면 작은 것 3개가 나온다
for idx, max in enumerate(top3, start = 1):
 print(f"{idx}번째, 값{max+1}")
