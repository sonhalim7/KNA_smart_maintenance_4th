py = "SIGNAL"
print(py[0], py[2], py[5])
print(py[-1], py[-2])
print(py[0:3],"/",py[3:6])
start = "temp_senor"
print(start[:4])
print(start[5:])
min = "sensor_01"
print(min[-2:])
print(py[::2])
print(py[::-1])
message = "설비 고장 발생"
print("고장" in message, '정상' in message )
num = "01012345678"
print(len(num))
count = "sensor-01-temp"
print(count.count('-'))
find = "temp_2024"
print(find.find('_'), "/", find.find('a'))
a = "sensor_log_csv"
print(a.startswith('sensor'), "/", a.endswith('csv'))
stat = "WARNING"
com = "warning"
print(stat == "WARNING", "/", stat == com)
r = "ready"
print(r.upper())
W = "WARNING"
print(W.lower())
name = "KIM CHUL SOO"
print(name.title())
f = "Fault"
F = "FAULT"
print(f == F, "->", f.lower() == F.lower())
work = " 가동중"
print(work.strip())
print("ABC".isupper(),"/", "abc".islower(),"/", "Abc".islower())
title = "Sensor_LOG_CSV"
print((title.lower()).startswith("sensor"), "/", (title.lower()).endswith("csv"))
a = " 대기 "
print(a.rstrip(),"/",a.lstrip())
warn = "***경고***"
print(warn, "->", warn.strip("*"))
w = " WARNING"
print(w, "->", w.strip(), "->", w.strip().lower())
s = " 경 보 "
st = s.strip()
print(s, "->",st)
a = "설비 정상 가동"
b = a.replace("정상", "점검")
print(b)
c = "PUMP 0A 03"
print(c.split())
a = "a, b, c, d"
print(a.split(","))
print(a.split(",", 1))