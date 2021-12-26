
# 1. парсер email, phone, name
# пользователь вводит строку, определить что он ввел - email, phone, name
# email - собака по середине, имя - не менее три буквы, доменная часть три буквы, точка три буквы
# abc@aaa.bbb
# phone - "+380631231212" плюс в начале и 12 цифр
# name - два слова через пробел, каждое с большой букв

string = input("Please write pattern: ").strip().lower()

list2 = string.split("@")

if len(list2) == 2 and len(list2[0]) == 3 and len(list2[1]) == 7 \
        and list2[0][0:3].isalpha() and list2[1][0:3].isalpha() \
        and list2[1][3] == "." and list2[1][4:7].isalpha():
    print("ok")
else:
    print("no")

stringTwo = input("Please write pattern: ").strip().lower()
print(stringTwo[1:13])

if len(stringTwo) == 13 and stringTwo[0] == "+" and stringTwo[1:13].isdigit():
    print("Ok")
else:
    print("No")

stringThree = input("Please write pattern: ").strip()

liststringThree = stringThree.split(" ")
print(liststringThree)

if len(liststringThree) == 2 \
    and liststringThree[0][0:5].isalpha() \
    and liststringThree[1][0:5].isalpha() \
    and len(liststringThree[0]) == 4 and len(liststringThree[1]) == 4\
    and liststringThree[0][0].isupper() and liststringThree[1][0].isupper():
        print("ok")
else:
    print("no")

#2. Дан list произвольных чисел (напр [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44,]).
# Написать программу, которая удалит из него все числа, которые меньше 18 и больше 81.

list = [11, 77, 4, 22, 0, 56, 5, 95, 7, 87, 13, 45, 67, 44]
print(id(list))

for i in list:
    if i < 18 or i > 81:
         list.remove(i)
print(list)
print(id(list))


# *3 Напишите программу, которая (аналогично заданию 1) проанализирует строку на номер телефона.
# Правила проверки - "+" впереди и 12 цифр за ним.

# **4. Ввести из консоли строку. Найти в строке самое длинное слово, в котором присутствуют подряд две согласные буквы.
# stringThree = input("Please write pattern: ").strip().upper()


def filter_(word, g):
    not_ = ''
    for i in word:
        if i in g:
            not_ += i
        else:
            not_ += ' '
    for lett in not_.split():
        if len(lett) >= 2:
            return word
    return ''


g = ('аоеиуэюя')
result = []
for word in 'пожаалуйста спасибо оочень доволен'.split():
    result.append(filter_(word, g))

print(max(result, key=len))


