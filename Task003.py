#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

#n = (input("Введите число: "))
#sum = 0
#while i < n:
#    a = (1 + 1 / i)**i
#    sum += a
#    print(a, sum)


n = int(input())
my_list = []
for i in range (1,n+1):
    my_list.append(round(((1 + 1 / i) ** i), 0))     # append закидывает в наш список эту формулу(с конца) (round округление)(0 в конце кол, знаков после запятой)
sum = 0
for i in range (n):
    sum = sum + my_list[i]
print (my_list, sum)
