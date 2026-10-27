#break 활용
#found = False
#n = int(input("횟수를 입력하세요 "))
#for i in range(n):
#    a = int(input("숫자를 입력하세요 "))
#    if a > 80:
#        found = True
#        break
#if found == True:
#    print("있음")
#else:
#    print("없음")

#for list
temp = [32, 29, 22, 31, 34]
for a in temp:
    if a > 30:
        print(f"{a}도 고온")

time = [8, 6, 9 ,10, 3, 5]
for b in time:
    if b >= 5 and b <= 10:
        print(f"{b}")

temp = [32, 36, 31, 28, 24]
count = 0
add = 0
for i in temp:
    if i > 30:
        count += 1
        add += i
print(f"{i} -> 합 {add}, 개수 {count}, 고온평균 {add/count}")

temp = [32, 31, 35, 33, 24]
list = []
for i in temp:
    if i > 30:
        list.append(i)
print(list, len(list))

temp = [24, 25, 21, 22, 27]
temp2 = []
for i in temp:
    a = i*1.8+32
    temp2.append(a)
print(temp2)

temp = [25, 35, 32, 28, 29, 31]
b = 0
d = 0
c = []
count = 0
total = 0
for i in temp:
    b += i
    d += 1
    if i > 30:
        c.append(i)
        count += 1
        total += i
print(f"전체평균{b / d}, 고온개수 {count}, 고온평균 {(total / count)}")

#tuple
sensor = ['모터온도', 78]
print(sensor[0])
print(sensor[1])
print(sensor[0:2])

sensor = [('a', 78), ('b', 75), ('c', 83), ('d', 67)]
for name, temp in sensor:
    if temp > 80:
        print(name, "경고")

sensor = [["a", 23, (4, 2)], ["b", 32, (5, 7)], ["c", 30, (7,1)], ["d", 28, (3, 5)], ["e", 33, (1, 6)]]
for q, r, s in sensor:
    print(s)
    if s[1] <= 5:
        print(r, "펌프압력")
    