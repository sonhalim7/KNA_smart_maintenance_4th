#set, add, union
id_a = ["S01", "S02", "S03", "S05", "S02", "S01"]
a = set(id_a)
print(sorted(a))
print(len(a))

#집합연산 (union, difference, intersection)
id_a = ["S01", "S02", "S03", "S05"]
id_b = ["S01","S02", "S04", "S06"]
a = set(id_a)
b = set(id_b)
print(f"모두: {sorted(a.union(b))}")
print(f"A만 : {sorted(a.difference(b))}")
print(f"B만 : {sorted(b.difference(a))}")
print(f"공통 : {sorted(a.intersection(b))}")

yes = ["S01", "S02", "S03"]
tod = ["S02", "S03", "S05"]
a = set(yes)
b = set(tod)
print(f"신규이상 : {b.difference(a)}")
print(f"지속이상 : {sorted(a.intersection(b))}")

#dictionary
sen = {"키" : 176}
print(sen["키"])
sen["새 키"] = 180
del sen["키"]
sen["기존 키"] = 176
print(sen)
print(sen.get("없는 키", 0))
print("기존 키" in sen)

sen = {"센서" : 3}
new = {"센서a" : 2, "센서b" : 1, "센서c" : 4}
sen.update(new)
del sen["센서"]
print(f"센서 수 : {len(sen)}")

sen = {"센서a" : 78, "센서b" : 92, "센서c" : 82, "센서d" : 71}
print(f"평균 : {sum(sen.values()) / len(sen)}")
max_value = 0
max_name = ""
for name, value in sen.items():
    if value > max_value:
        max_value = value
        max_name = name
print(max_name, max_value)

sen = ["a", "b", "c"]
value = [13, 15, 19]
a = dict(zip(sen, value))
for name, num in a.items():
    print(name, num)

a = {"온도" : 32, "압력" : 81, "작동시간" : 31}
b = {"온도" : 40, "압력" : 60, "작동시간" : 15}
c = []
for name, num in a.items():
    for d, e in b.items():
        if name == d and num >= e:
            c.append(name)
            c.append(num)
print(f"경고센서 : {c}")

db = { "1번 펌프" : {"압력" : 91, "상태" : "비정상"}, "2번 펌프" : {"압력" : 76, "상태" : "정상"},  "3번 펌프" : {"압력" : 86, "상태" : "비정상"}}
print(db["2번 펌프"]["상태"])
for name, info in db.items():
    if info["상태"] == "비정상":
        print(f"점검필요 {name}")

a = ["온도,78", "압력,72", "진동,35"]
b = {}
for c in a:
    d, e = c.split(",")
    b[d] = e
print(b)

# 이건 dictinary 내부 변수 이름이 같아서 item으로 name을 나누고 사용할 수 있었지만
# 변수 이름이 다르다면 b도 item으로 나눠서 따로 진행해야한다.
# ex a, b in a.items() c,d in e.items()
# if (a == "온도" and c == "기계온도") == "TRUE"
#   if b > d: append.(b) 이런식으로
a = {"온도" : 32, "압력" : 81, "작동시간" : 31}
b = {"온도" : 40, "압력" : 60, "작동시간" : 15}
k = []
print(f"평균 : {sum(a.values()) / len(a)}")
for name, num in a.items():
        if num > b[name]:
            k.append(name)
print(f"위혐센서 : {k}")