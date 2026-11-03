#raise
def check_value(text, lo = 0.0, hi = 5000.0):
    v = float(text)
    #TODO : 범위 밖이면 ValueError 발생
    if not (lo <= v <= hi):
        raise ValueError(v, "정상 범위 밖")
    return v

for i in ["128.5", "결측", "-999"]:
    try:
        print("통과: ", check_value(i))
    except ValueError as e:
        print("제외 :", e)