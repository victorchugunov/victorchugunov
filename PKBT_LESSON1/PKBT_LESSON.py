cnt = 1
for x in range (1, 1000000, 2):
    is_x_prime = x != 1
    for n in range (2,x):
        if (x % n) == 0:
            is_x_prime = False
            break
    if is_x_prime:
        cnt += 1
     
print (cnt/10000)

        #посчитать процент простых чисел от 1 до миллиона