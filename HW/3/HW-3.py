# 1. Есть list с данными ( например lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
# . Напишите код, который формирует новый list (например lst2), который содержит только переменные-строки, которые есть в lst1.

list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
listNew = []
for i in list:
    if type(i) is str:
        listNew.append(i)
print(listNew)

# 2. Ввести из консоли строку. Определить количество слов в этой строке, которые начинаются на букву
# "а" (учтите, что слова могут начинаться с большой буквы).
string = (input("Please write word: ")).split(" ")

print(string)
count = 0
for i in string:
    if i.strip().lower().startswith("a"):
        count += 1
print(count)

sentence = " ".join(string)
print(sentence)

# *Вывести пользователю приветствие ('Hello!'). Спросить у пользователя, хочет ли он повторно его увидеть этот текст?
# Если пользователь введет Y - повторить приветствие и спросить еще раз (спрашиваем каждый раз как пользователь ввел Y)
# . Если если пользователь введет N - прекратить спрашивать. Если пользователь ввел не Y или N - переспрашивать, пока не введет Y или N.
#
while True:
    print("Hello Bro")
    print("Would you like to see this massage?")
    enterInvite = input("Please write y or no ").strip().lower()
    if enterInvite == "y":
        continue
    elif enterInvite == "n":
        break
    else:
        continue

