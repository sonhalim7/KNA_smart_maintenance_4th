#join 함수
# '구분자'.join(리스트) -> 구분자가 먼저 와야한다.
a = ["2015", "01", "15"]
print("-".join(a)) #2015-01-15
print("2015", "01", "15", sep = "-")
print("2015", "01", "15", sep = ",")
#split, join 같이 쓰기
date = "2015/01/15"
s = date.split("/")
print(s, "->", "-".join(s))
b = "1, NORMAL, 25.3"
c = b.split(",")
print(c[1].lower().split())

a = "PUMP_A"
b = 87
print(f"설비{a}, 온도{b}")
a = 80
b = 74
c = 92
print(f"평균점수는 {round((a+b+c)/3, 2)}")
value = 87.456
print(f"소숫점 한 자리{value:.1f}")
print(f"소숫점 두 자리{value:.2f}")
a = " 5, sensor_2, WARNING, 0.78912 "
b = a.strip()
c = b.split(",")
print(f"센서{c[1]} 상태{c[2].lower()}, 측정값{float(c[3]):.2f}")
temp = [25, 26, 24 ,23, 27]
a = []
print(temp, len(temp), a, len(a))
temp = [24, 25, 26, 22, 26, 29]
print(temp[0], temp[2], temp[5])
temp = [25, 23, 22, 19, 29, 20]
a = temp[0]
b = temp[5]
print(a+b, (a+b)/2)
temp = [12, 24, 24, 15, 17, 18, 20, 29, 10, 29]
print(temp[0:3], len(temp[0:3]))
print(temp[6:9], len(temp[6:9]))
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
first = num[0:6]
second = num[6:12]
print(first, "/", len(first))
print(second, "/", len(second))
temp = [24, 25, 25, 27, 240, 21]
print(240 in temp)
temp[4] = 24
print(temp, 240 in temp)
a = []
a.append(13)
a.insert(0, 14)
d = [15, 20]
a.extend(d)
print(a)

temp = [25, 24, 26, 999, 23, 29]
temp.remove(999)
pop = temp.pop(2)
print(temp, "/", pop)
print()
temp = [19,30, 21, 25, 18, 29, 30, 24]
temp.sort()
print(temp)
temp.reverse()
print(temp, "/", temp.count(30),"/", temp.index(30))


