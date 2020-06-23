i = 0
while i <= 5:
    print('黑马你好')
    i += 1
i **= 3
print(i)
i, j = 0, 0
sum1, sum2 = 0, 0
while i <= 100:
    if i % 2 == 0:
        sum1 += i
    i += 1
    if i == 50:
        break
print(sum1)
while j <= 100:
    if j == 3:
        continue
    if j % 2 == 0:
        sum2 += j
    j += 1
    if j == 50:
        break
print(sum2)
