m = []
def sumpro():
    print("Вводите числа через пробел")
    s = 0
    p = 1
    for i in input().split():
        m.append(int(i))
    for g in range(len(m)):
        if m[g] > 0:
            s += m[g]
    Mmin = min(m)
    lo = m.index(Mmin)
    Mmax = max(m)
    ma = m.index(Mmax)
    if lo > ma:
        lo, ma = ma, lo
    print(lo, ma)
    for j in range(lo + 1, ma):
        p *= m[j]
    return s, p
result = sumpro()
print(result)
