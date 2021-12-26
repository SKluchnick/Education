# 1.Написать функцию, принимающую один аргумент.
# Функция должна вывести на экран (c помощью print) тип данных этого аргумента (type)

# def translater_of_type(value):
#     print(type(value))
#
# translater_of_type("sdfgh")

# 2. Написать функцию, принимающую два аргумента. Функция должна
# - если оба аргумента относятся к числовым типам (int, float) - вернуть их произведение
# - если к строкам - соединить в одну строку и вернуть
# - если первый строка, а второй нет - вернуть словарь (dict), в котором ключ - первый аргумент, значение - второй
# в любом другом случае вернуть кортеж (tuple) из аргументов
#
# def calculate_of_type(valueFirst,valueSecond):
#     if type(valueFirst) == int and type(valueSecond) == int:
#         return  valueFirst * valueSecond
#     elif type(valueFirst) == str and type(valueSecond) == str:
#         return valueFirst + valueSecond
#     elif type(valueFirst) == str and type(valueSecond) != str:
#         return ({valueFirst:valueSecond})
#     else:
#         return (valueFirst,valueSecond)
#
# res = calculate_of_type(1,"2")
# print(type(res))
# print(res)


# Дан словарь продавцов и цен на какой то товар у разных продавцов
# : { ‘citrus’: 47.999, ‘istudio’ 42.999, ‘moyo’: 49.999, ‘royal-service’: 37.245, ‘buy.ua’: 38.324, ‘g-store’: 37.166, ‘ipartner’: 38.988, ‘sota’: 37.720 }.
# Написать функцию возвращающую список имен продавцов, чьи цены попадают в определенный диапазон.
# Функция должна принимать словарь, начало и конец диапазона и возвращать список имен.

# def price_value (one,two,*dct):
#     if type(dct) == dict:
#         return
#         dct = {}
#     for x in dct:
#         for i,j in x.items():
#             if j >= one and j <= two:
#                 print(i, j)
#
# price_value (30,39,{ 'citrus': 47.999, 'istudio': 42.999, 'moyo': 49.999, 'royal-service': 37.245,
# 'buy.ua': 38.324, 'g-store': 37.166, 'ipartner': 38.988, 'sota': 37.720 })



#4 * Пользователь вводит строку произвольной длины.
# Написать функцию, которая должна вернуть словарь следующего содержания: ключ - количество букв в слове, значение - список слов с таким количеством букв.
# Отдельным ключем, например "0", записать количество пробелов
# . Отдельным ключем, например "punctuation", записать все уникальные знаки препинания, которые есть в тексте. Например:



# def compressed (word):
#   letter_dict = {}
#   count = 0
#   for letter in word:
#     if letter not in letter_dict:
#         count = 1
#         letter_dict[letter] = count
#     else:
#         count += 1
#         letter_dict[letter] = count
#   return letter_dict
#
# print (compressed("aaaarggh sdfgaaaaaaaaaa"))



def compressed (word):
    countFirst = 0
    letter_dict = {}
    for i in word:
        if i == ".":
            countFirst +=1
            letter_dict[i] = countFirst
            letter_dict["punctuation"] = letter_dict.pop(".")
        if  i == ",":
            countFirst +=1
            letter_dict[i] = countFirst
            letter_dict["punctuation"] = letter_dict.pop(",")
    word2 = word.replace("."," ").replace(","," ").split(" ")
    for letter in word2:
        countThird = len(letter)
        letter_dict[letter] = countThird

    return letter_dict

print (compressed("aaa.arg,ghs.dfg,aaaa.aaaaaa.ghjk"))


