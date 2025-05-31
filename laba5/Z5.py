def ur():
    print("(a+4*b)*(a-3*b)+a*2")
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = (a+4*b)*(a-3*b)+a*2
    return c
result = ur()
print(result)