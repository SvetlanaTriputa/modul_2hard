n=int(input('Введите число от 1 до 20 '))
result = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if j > i and n % (i+j) == 0:
            result.append(i)
            result.append(j)

    result1 = ''
    for p in result:
        result1 += str(p)

print ('Шифр:',result1)