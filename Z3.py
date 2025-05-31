import random
m = []
randNum = random.randint(5, 15)
for i in range(randNum):
    randomNumber = random.randint(1, 100)
    if randomNumber % 2 == 0:
        m.append(randomNumber)
print(m)