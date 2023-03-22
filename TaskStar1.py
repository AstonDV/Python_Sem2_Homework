# *** (1)У вас есть массив чисел, составьте из них максимальное число. 

# Например: [61, 228, 9] -> 961228

# original_array = [61, 228, 9]

from random import randint

n = int(input("Введите количество элементов массива: "))
min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))
array = [randint(min, max) for _ in range(n)]
print ("Заданный массив чисел: " + str(array))

def key_func(num):
	return str(num)*3

sorted_list = sorted(array, key=key_func, reverse=True)
largest_number = "".join([str(num) for num in sorted_list])
print("Максимальное число:", largest_number)
