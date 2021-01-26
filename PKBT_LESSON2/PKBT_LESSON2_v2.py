#task1 написать функцию 1/math.log(N)
#task2 написать функцию, возвращающую список множителей аргумента
#task3 построить график (посчитать) разницы между реальным
#значением процента простых чисел и асимптоты

import math

def asymptote(x): #функция вычисления количества простых чисел от 1 до аргумента
    result = (x/math.log(x))
    return result
    
def factoring(x): #функция определения списка множителей аргумента
    factor = []
    divider = 2
    while x >= math.sqrt(divider):
        if x % divider == 0:
            factor.append(divider)
            x = x/divider
        else:
           divider += 1
    if x > 1:
        factor.append(x)
    return factor

def prime_counter(x): #функция подсчёта простых чисел от 1 до аргумента
    count = 0
    for d in range(1, int(x)):
        is_x_prime = d != 1
        
        for n in range(2, round(math.sqrt(d)+1)):
            if (d % n) == 0:
                is_x_prime = False
                break

        if is_x_prime:
            count += 1
    return count

while True:
    end = int(input ("end = ")) #ввод верхней границы "графика"

#график строим с шагом 10 от 10 до end
    for N in range (10, int(end), 10):   
        print ("N = ", N)
        print("difference = ",round(prime_counter(N)-asymptote(N),2)) #разница значений количества простых чисел
        #print("#"*int(round(count-asymptote(N)))) #принт графика

        #список множителей числа "end":
    print("factor 'end' = ", factoring(end))
