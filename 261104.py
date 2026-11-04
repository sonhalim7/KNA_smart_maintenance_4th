#NumPy숫자묶음계산 -> 가장기초
#Pandas표데이터처리 -> NumPy 기반
#Matplotlib그래프시각화 -> NumPy 기반

import numpy as np
#리스트 vs 배열
#1)리스트
# - 서로다른 자료형도 같이 존재가능
# - 계산이 느리고 반복문을 돌아한다
list = [70, 71, 72]
print(list * 2)
print([v * 2 for v in list])
#2)배열
#- 같은 자료상만 존재가능
#- 계산이 빠르다

temp = np.array([70,71,72])
print(temp)
print(temp+2)
#튜플로 배열만들기
print(np.array((1,2,3)))

temp = np.array([22, 24, 26, 29, 31])
print(temp)
n_temp = temp * 1.8 + 32
print(n_temp)

#np.array -> 값을알때센서측정값
#np.arange -> 간격필요측정시점
#np.linspace - > 개수를정함그래프축
#np.zeros -> 0으로채움빈그릇
#np.full -> 특정값으로채움기준값설정

light = np.linspace(0, 70, 8)
print(light)

num = np.arange(0, 40, 5)
print(num)

#ndim 차원개수
#shape 행·열크기
#size 값총개수
#dtype 자료형
#astype = 자료형 바꾸기
temp = np.array([[32,4],[12, 6],[18, 3],[22, 7]])
print(f"차원 {temp.ndim}")
print(f"형태 {temp.shape}")
print(f"개수 {temp.size}")

a = np.array([[12.8], [13.6], [27.2], [19.1]])
print(a.dtype)
b = a.astype(int)
print(b.dtype)
print(b)

#reshape = 행 열 모양다시 잡기
#flatten = 모양 다시 1자로 잡기
cycle = np.array([14, 25, 12, 16, 43, 32, 12, 19, 20, 65, 93, 83])
re_cycle = cycle.reshape(3, 4)
print(cycle)
print(re_cycle)

cal = np.array([[23, 6, 128], [32, 7, 321], [19, 2, 293], [34, 5, 532]])
re_cal = cycle.reshape(4,3)
print(re_cal)
flat_cal = re_cal.flatten()
print(flat_cal)

#index, slicing
tok = np.array([32, 42, 53, 68, 45, 41, 23, 74, 11, 74])
print(f"처음{tok[0]}, 마지막{tok[-1]}, 중간 구간{tok[1:4]}")
print(f"건너뛰기 {tok[1::2]}")

tok = np.array([[164, 42], [1234, 64], [127, 95], [9824, 32]])
th_tok = tok[2]
print(th_tok)
print(tok[:, [0]]) # 세로로 출력
print(tok[:, [1]])  # 가로로 출력하려면 print(tok[:, 1]) 이런식으로
# print(tok[0, :]) 1행 출력