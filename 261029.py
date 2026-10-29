def greet():
    print("점검을 시작합니다.")
greet()
greet()

print("A 설비")
print("이상 없음")
print("B 설비")
print("이상 없음")
print("C 설비")
print("이상 없음")
def check_machine():
    print("이상 없음")
print("A설비")
check_machine()
print("B설비")
check_machine()
print("C설비")
check_machine()

def check(temp1, temp2):
    print(f"모터{temp1}도, 펌프{temp2}도")
check(78, 92)

def check(temp2, temp1):
    print(f"모터{temp1}도, 펌프{temp2}도")
check(78, 92)

def report(device, value):
    print(f"{device}{value}")
report(device = "모터", value = 82)
report(device = "펌프", value = 92)
report(value = 92, device = "모터")

#return
def calc(a, b):
    return(a+b) / 2
avg = calc(90, 80)
print(avg)
print(avg + 5)

def sensor(values):
    return min(values), max(values), sum(values)/len(values)
calc = sensor([78, 92, 85])
print(calc)

def check(score, limit = 90):
    if score >= limit:
        return "경고"
    else:
        return "정상"
print(check(78))
print(check(95))
print(check(50, limit = 50))

def test():
    a = 30
    print("함수 안", a)
test()

def cal_avg(scores):
    return sum(scores) / len(scores)

def eva_avg(avg):
    if avg >= 80:
        print(f"평균{avg}-> 정상")
    else:
        print(f"평균{avg}-> 평균이하")
input_scores = [90, 80]

result_avg = cal_avg(input_scores)

eva_avg(result_avg)