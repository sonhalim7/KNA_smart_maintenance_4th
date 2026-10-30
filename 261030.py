#모듈 / 패키지 / 라이브러리
# 모듈 : 기능을 모아둔 .py 파일
# 패키지 : 모듈을 모아둔 폴더
# 라이브러리 : 위에 사항들을 통칭

# import 방식
# 형식 : import 모듈
import math
print(math.sqrt(16))
print(math.ceil(4.2))
from math import sqrt, ceil #일부만 불러옴 -> 모듈명 없이 바로 사용가능
print(sqrt(16), ceil(4.2))
import math as m
print(m.sqrt(16))
print(m.ceil(4.2))

#표준 라이브러리 -math / random / datetime
# - 파이썬 설치 시 함꼐 깔리는 검증된 모듈들
import random
import datetime

print(random.randint(1,100))
print(datetime.datetime.now())
a = random.randint(1,100)
print(a)
print(math.sqrt(a))

# 경로와 os 모듈
#1. 절대경로 - 전체주소
#2. 상대경로 - 실행중인 위치를 기준으로 한 주소
import os
print("현재 실행 위치(절대경로): ", os.getcwd())

#폴더 유무 확인
print(os.path.exists("data"))

#폴더 목록 확인
files = os.listdir("data")
print(files)

import os
print("현재 작업 폴더 확인 : ", os.getcwd())
print(os.listdir("data"))
files = os.listdir("data")

for name in files:
    if name.endswith(".csv"):
        print(name)

# 폴더명 + 파일명 -> 경로
path = os.path.join("data","08_press.csv")
if os.path.exists(path):
    print("파일 경로: ", path)

import os
path = os.path.join("data", "python.py")
print(os.path.exists(path))
if os.path.exists(path):
    print("파일 존재", path)
else:
    print("파일 없음")

import os
import datetime
a = len(os.listdir("data"))
b = datetime.datetime.now()
print(f"파일 {a} 개, 점검시각 {b}")

import os
files = os.listdir("data")
list = []
for names in files:
    if names.endswith(".csv"):
        list.append(names)

print(f"파일목록 {list}")

# 파일 입출력
# open()
# 형식 : open(파일명, 모드, encoding)
# 모드 : r -> 읽기, w -> 새로쓰기, a -> 이어쓰기
# encoding = 'utf-8' 한글이 깨지지 않도록 하는 것

FILE = "data/08_press.csv" #상수(변하지 않는 값 대문자로 표현)
f = open(FILE, "r", encoding='utf-8')
text = f.read()
f.close()
print(text)

#with open - 블록이 끝나면 자동으로 닫힌다
with open(FILE, "r", encoding = 'utf-8') as f:
    for line in f:
        print(line)

#with open("FILE", "w", encoding="utf-8") as file:
#    file.write("안녕하세요, 새로운 내용입니다.\n")A
#    file.write("기존에 이 파일이 있었다면, 그 내용은 모두 지워졌습니다.\n")

with open(FILE, "a", encoding = 'utf-8') as k:
    k.write("a 모드 테스트\n")
    k.write("내용보존확인") 
print(k)

import csv
with open(FILE, "r", encoding = 'utf-8') as v:
    reader = csv.reader(v)
    for line in reader:
        print(line)

import csv
with open(FILE, "w", encoding = 'utf-8', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(["csv writer 점검", "출력확인"])
print(f)