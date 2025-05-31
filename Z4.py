text = input()
result = list(text)
if result[0] == 'a' and result[1] == 'b' and result[2] == 'c':
    result[0] = 'w'
    result[1] = 'w'
    result[2] = 'w'
else:
    result.append("zzz")
print("".join(result))