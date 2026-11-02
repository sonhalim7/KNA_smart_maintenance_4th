#예외 확인
#트레이스백

#try except
#temp = input("온도 입력 : ")
#try:
#    a = int(temp)
#    print(a)
#    print("프로그램은 계속됩니다.")
#except:
 #   print("숫자를 입력하세요")
 #   print("프로그램은 계속됩니다.")

#ValueError-값이부적절int("스물")
#FileNotFoundError-파일이없음open 실패
#ZeroDivisionError - 0으로나눔평균계산시데이터0개
#IndexError-범위초과칸이부족한줄
#KeyError-없는키접근딕셔너리검색
#TypeError-값종류가틀림10 + "개
#num = input("측정값 입력 : ")
#try:
#    a = int(num)
#    print(100/a)
#except ValueError:
#    print("숫자가 아닙니다.")
#except ZeroDivisionError:
#    print("0으로 나눌 수 없습니다.")

FILE_ERROR = "data/09_ict_inspection_dirty.csv"
FILE = "data/09_ict_inspection.csv"
#f = open(FILE, 'r', encoding = 'utf-8')
#try:
#    raise RuntimeError("처리 도중 예외 발생!")

#finally:
#    f.close()
#    print("파일 닫힘")

try:
    with open (FILE_ERROR, encoding = 'utf-8') as f:
        rows = f.readlines()[1:]
except FileNotFoundError:
    rows = []

total = 0.0
skip = 0
for line in rows:
    try:
        total += float(line.split(",")[2]) # 측정값 2열
    except (ValueError, IndexError):
        skip += 1
        continue

print("합계", round(total, 1), "건너뜀", skip)

#실습3
number = input("측정값 입력")
rows = number.split(",")
total = 0.0
skip = 0
for i in rows:
    try:
        total += float(i.strip())
    except ValueError:
        skip += 1
        continue

print("총합계: ", total, "건너뛴 수: ", skip)

#실습4
file_list = ["data/08_press.csv", "data/09_ict_inspection_dirty.csv", "data/09_ict_inspection.csv", "datadata"]
count = 0
error = 0
for name in file_list:
    try:
        with open(name, 'r', encoding = 'utf-8') as k:
            count += 1
    except FileNotFoundError:
        error += 1
        continue

print("처리한 파일 수: ", count, "없는 파일 수 : ", error)
