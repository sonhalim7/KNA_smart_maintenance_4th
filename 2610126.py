#입력받는 함수  input
#age = int(input("나이를 입력하세요"))
#if age >= 19: #if else 둘다 :로 끝내기
#    print("성인입니다.")
#else:
#    print("미성년자입니다.")

# 점수 파악
#score = int(input("점수를 입력하세요"))
#if score >= 90: 
#    print("A")
#elif 80 <= score < 90:
#    print("B")
#elif 70<= score < 80:
#    print("C")
#else:
#    print("F")
#tem = int(input("온도를 입력하세요 "))
#if tem > 80:
#    print("위험")
#elif tem > 60 and tem <=80:
#    print("주의") 
#else:
#    print("정상")
#id = "admin"
#pas = 1234
#log = input("아이디를 입력하세요 ")
#word = int(input("비밀번호를 입력하세요 "))
#if log == id and word == pas:
#    print("로그인 성공")
#else:
#    print("로그인 실패")
#tem = int(input("온도를 입력하세요 "))
#a = float(input("진동을 입력하세요 "))
#A = int(input("전류를 입력하세요 "))
#if tem > 80 or a > 4.0:
#    print("위험: 즉시정지")
#elif A > 60 and tem > 70 
#    print("주의: 부하점검")
#elif A > 2.5:
#    print("주의: 진동관찰")
#else:
#    print("정상")

#for문
#N = int(input("숫자를 입력하세요 "))
#for i in range(1, N+1):
#    print(i)
#print()
#for i in range(1, N+1, 2):
#    print(i)
#print()
#for i in range(N, 0, -1):
#    print(i)

#N = int(input("숫자 입력 "))
#add = 0
#for i in range(1, N+1):
#    add += i
#print(add)

#구구단 만들기
#for i in range(2, 10):
#    for a in range(1, 10):
#        print(f"{i} x {a} = {i*a}")
#        if a == 9:
#            print(f"{i} x {a} = {i*a}\n")

#count = int(input("측정횟수 입력 "))
#num = 0
#for i in range(0, count):
#    a = int(input("측정값 입력 "))
#    if a > 80:
#        num += 1
#print("초과 개수 : ", num)

#while
a = 7
b = 0
while a != b:
    b = int(input("숫자를 입력하세요 "))
print("정답입니다!")
