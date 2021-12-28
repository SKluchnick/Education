# TODO 1.Напишите программу которая на вход принимает список чисел и проверяет все ли числа
# TODO в этой последовательности являются уникальными


def buildList(date):
    if not (isinstance(date, list)):
        return
    lst2 = []
    for i in date:
        if isinstance(i, int):
            lst2.append(i)
    return lst2


j = buildList([1,2,'ki',3,4,5,'jjj',58])
j = buildList(57)
print(j)

def checkerOfNumbers(date):
    if not (isinstance(date, list)):
        return
    lst2 = []
    for i in date:
        if isinstance(i, int):
            lst2.append(i)
            for j in lst2:
                counter = lst2.count(j)
                if counter > 1:
                    break
    print(f'We have doubles {i}')
    return counter


print(checkerOfNumbers([1, 2, 'jjj', 587, 'jjj', 2, 2, 2, 2]))


print(checkerOfNumbers(1))


def balance(lst):
    lst2 = []
    set1 = set()
    for ik in lst:
        lst2.append(ik)
        set1.add(ik)
    if len(lst2) != len(set1):
        return False
    else:
        return True


res = balance([1, 2, 3, 4, 5, 6,6,6,6,6])
print(res)

def balance(lst):
    return len(set(lst)) == len(lst)


print(balance([1,2,3,4,4,4,4]))

# TODO 2.Напишите функцию которая принимает dict и преобразовует его в список

def convertDictToList(d):
    lst = []
    for i, j in d.items():
        lst.append(i)
        lst.append(j)
    return lst


print(convertDictToList({'g': 1, 'l': 4}))

def convertDictToList(d):
    lst = []
    lst2 = []
    for i, j in d.items():
        lst.append(i)
        lst2.append(j)
    return lst, lst2


print(convertDictToList({'g': 1, 'l': 4}))

def convertDictToList2(d):
    lst = []
    for j in d.items():
        lst.append(list(j))
    return lst

l =convertDictToList2({'citrus': 48, 'istudio': 42.999, 'moyo': 50, 'royal-service': 37.245,
             'buy.ua': 38.324, 'g-store': 37.166, 'ipartner': 38.988, 'sota': 37.720})
print(l)


def convertDictToList2(dct):
    return (list(i) for i in dct.items())

print(convertDictToList2({'citrus': 48, 'istudio': 42.999, 'moyo': 50, 'royal-service': 37.245,
             'buy.ua': 38.324, 'g-store': 37.166, 'ipartner': 38.988, 'sota': 37.720}))

# TODO 3.Написать функцию которая найдет сумму элементов списка умноженных на свой индекс

def calculateSumIndex(dct):
    sum = 0
    for i in dct:
        sum += i * dct.index(i)


    return sum



print(calculateSumIndex([1, 2,3,4]))


def calculateSumIndex(dct):
    sum = 0
    ind = 0
    for i in dct:
        print(f'индекс {i}')
        sum += i * ind
        ind += 1
        print(sum)

    return sum


print(calculateSumIndex([1, 2,3,4]))


def calculateSumIndex(dct):
    sum = 0
    for i in range(len(dct)):
        print(i)
        print(dct[i])
        sum += i * dct[i]
    return sum
print(calculateSumIndex([10,4]))

# TODO 4.В списке все Элементы различные поменять местами max и min списка создавать новый список запрещено
def changeValues(lst):
    max = 0
    min = 1000
    for i in lst:
        if i > max:
            max = i
            indOne = lst.index(max)
        if i < min:
            min = i
            indTwo = lst.index(min)
    lst[indOne] = min
    lst[indTwo] = max

    return lst


i = changeValues([10, 15,1000,1, 25 ])
print(i)
