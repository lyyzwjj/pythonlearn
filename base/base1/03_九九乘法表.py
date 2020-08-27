m = 1
while m <= 5:
    n = 1
    while n <= m:
        print('*', end='')
        n += 1
    print('')
    m += 1
    
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d*%d=%d '%(i,j,i*j),end='\t')# \t对齐 \n换行
        j += 1
    print('')
    i += 1

