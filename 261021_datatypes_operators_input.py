# 자료형
count = 3
print(count)
temp = 3.1
print(temp)
str = "python"
print(str)
is_okay = 3>2
print(is_okay)
print(type(count))
print(type(temp))
print(type(str))
print(type(is_okay))
print(type (100)) # int 
print(type (100.0)) #float 
print(type("100")) #str
print(4+5)
print("4"+"5")
print("45"+"67")
#3>2 비교
print(3>2)
print(5 == 5)
print(type(3>2))
a = 7
print(type(a))
a = 3.5
print(type(a))
a = "자료형"
print(type(a))
device_temp = 123.3
device_count = 12
device_name = "K_뉴딜"
is_normal = 1>2
print(type(device_temp), type(device_count), type(device_name), type(is_normal))
print()
a = 17
b = 5
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)
#점수
a = 90
b = 100
c = 87
print("평균 : ", round((a+b+c)/3,4))
#넓이
print("넓이 : ", a*b, "부피 : ", a*b*c)
#비교 연산자
a = 4.5
b = 5.7
print(a == b, a != b, a > b, a < b, a >= b, a <= b)
temp = 85
a = 60 <= temp <= 90
pre = 5
b = 3 <= pre <=7
print (a, b)

# 재고 파악
a = 100
b = a+50
c = b-30
d = c+5
print(a, "->", b, "->", c, "->", d)
#생산데이터
good = 500
bad = 23
per = (bad / good) * 100
whole = 24
role = 21
per2 = (role / whole) * 100
print("불량률", per,"%","가동률", per2, "%")
# 시간
time = 500
hour = 500 // 60
minute = 500 % 60
print(hour, "시", minute, "분")

#이름
#name = input("이름: ")
#print("안녕하세요", name, "님!")
#year= int(input("태어난 해 입력: "))
#age = 2026 - year
#print("나이 :", age, "살")

#국가
#country = input("거주 국가 : ")
#town = input("거주 도시 : ")
#print('저는 ', country, town,"에 삽니다.")

#에러 메시지
#age = int(input("나이: "))
#print(age)
#temp = int(input("온도 입력 :"))
#print("고온 주의 : ", temp >30)
#print("저온 주의 : ", temp < 20)

a = int(input("국어 점수 : "))
b = int(input("수학 점수 : "))
c = int(input("영어 점수 : "))
avg = (a+b+c)/3
print("평균 이상 : ",int(avg),  avg >= 80)
print("평균 이하 : ",int(avg),  avg < 80)