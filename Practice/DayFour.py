#TODO 1. С клавиатуры вводится число n - размер массива. Необходимо создать массив
# указанного размера и заполнить его случайными числами от 0 до 10. Затем вывести
# содержимое массива в консоль, а также вывести в консоль информацию о:
# а) Длине массива
# б) Количестве чисел больше 8
# в) Количестве чисел равных 1
# г) Количестве четных чисел
# д) Количестве нечетных чисел
# е) Сумме всех элементов массива
# Пример:
# Введено число 10. Сгенерирован следующий массив:
# [4, 8, 4, 9, 5, 2, 2, 3, 3, 6]
# Информация о массиве:
# Длина массива: 10
# Количество чисел больше 8: 1
# Количество чисел равных 1: 0
# Количество четных чисел: 6
# Количество нечетных чисел: 4
# Сумма всех элементов массива: 46
import random

enter = int(input('Please write num: '))

def array():
    array = []
    for i in range(enter):
        array.append(random.randint(1, 27))
    return array
res  = array()
print(res)


print()

def lenArray():
    newArray = res
    lenArray = len(newArray)
    return lenArray
reslenArray = lenArray()
print(f'Длина массива: {reslenArray}')



print()

def moreThan8():
    newArray = res
    print(newArray)
    count = 0
    for i in newArray:
        if i > 8:
            count += 1
    return count
resmoreThan8 = moreThan8()
print(f'Количество чисел больше 8: {resmoreThan8}')


print()

def equalsOne():
    newArray = res
    print(newArray)
    count = 0
    for i in newArray:
        if i == 1:
            count += 1
    return count
resequalsOne = equalsOne()
print(f'Количество чисел равных 1: {resequalsOne}')

print()

def equalsBalanceFromTwo():
    newArray = res
    print(newArray)
    count = 0
    for i in newArray:
        if i % 2 == 0 and i != 0:
            count += 1
    return count
resequalsBalanceFromTwo = equalsBalanceFromTwo()
print(f'Количество чисел кратных 2: {resequalsBalanceFromTwo }')


print()

def equalsBalanceFromThree():
    newArray = res
    print(newArray)
    count = 0
    for i in newArray:
        if i % 3 == 0 and i != 0:
            count += 1
    return count
resequalsBalanceFromThree = equalsBalanceFromThree()
print(f'Количество чисел кратных 3: {resequalsBalanceFromThree}')


print()

def equalsSumArray():
    newArray = res
    print(newArray)
    sum = 0
    for i in newArray:
        sum += i
    return sum
resequalsSumArray = equalsSumArray()
print(f'Сумма чисел: {resequalsSumArray}')