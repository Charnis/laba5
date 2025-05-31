m = []
n = int(input())
result = 0
for i in range(1,n+1):
    m.insert(i, i)
print(m)
for j in range(len(m)):
    if m[j] != 1 and m[j] != n:
        result += m[j]
print(result)