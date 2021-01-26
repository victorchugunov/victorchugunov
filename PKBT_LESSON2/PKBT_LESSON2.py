#task1 написать функцию 1/math.log(N)
#task2 написать функцию, возвращающую список множителей аргумента
#task3 построить график (посчитать) разницы между реальным
#значением процента простых чисел и асимптоты

import math

def asymptote(X): #функция вычисления количества простых чисел от 1 до аргумента
    result = (X/math.log(X))
    return result
    
def factoring(Y): #функция определения списка множителей аргумента
    factor = []
    divider = 2
    while Y >= math.sqrt(divider):
        if Y % divider == 0:
            factor.append(divider)
            Y = Y/divider
        else:
           divider += 1
    if Y>1:
        factor.append(Y)
    return factor

end = int(input ("end = ")) #ввод верхней границы "графика"

#график строим с шагом 10 от 10 до end
for N in range (10, int(end), 10):
    count = 0
    for x in range(1, int(N)):
        is_x_prime = x != 1
        
        for n in range(2, round(math.sqrt(x)+1)):
            if (x % n) == 0:
                is_x_prime = False
                break

        if is_x_prime:
            count += 1
    print ("N = ", N)
    print("difference = ",round(count-asymptote(N),2)) #разница значений количества простых чисел

    #print("#"*int(round(count-asymptote(N)))) #принт графика

    #список множителей числа "end":
print("factor 'end' = ", factoring(end))
