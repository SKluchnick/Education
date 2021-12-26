#1. Используя переменные a и b сформировать строку
# "First variable is [тут знаение переменной a], second variable is [тут знаение переменной b]. " \
# "Their sum is [тут их сумма]. Переменные получите с помощью input()

EnterFirstDigit = input("Please enter first digit: ")
EnterSecondDigit = input("Please enter second digit: ")
print("First variable is :" + EnterFirstDigit + " second variable  :" + EnterSecondDigit)
print(f"Their sum is : {int (EnterFirstDigit) + int( EnterSecondDigit)}")

# 2.Попросить пользователя ввести из консоли свой возраст.
# если пользователь ничего не ввел (ввел пустую строку) - вывести “не понимаю”
# если пользователю меньше 7 - вывести “где ваши мама и папа?”
# если пользователю меньше 18 - вывести “мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “вы в зоне риска”
# в любом другом случае - вывести “оденьте маску!”

EnterAgeOfUser = input("Please write your age: ")
if EnterAgeOfUser == "":
    print("I do not understand")
elif int(EnterAgeOfUser) < 7:
    print("Where is your mother or father")
elif int(EnterAgeOfUser) < 18:
    print("We do not sell cigarettes for teenagers")
elif int(EnterAgeOfUser) > 85:
    print("You are in dangerous zone")
else:
    print("Put masc please")


# * Усложнение задания 2, сделайте отдельным заданием. Попросить пользователя ввести из консоли свой возраст.
# если пользователю меньше 7 - вывести “Тебе [x] [year], где твои мама и папа?”
# если пользователю меньше 18 - вывести “Тебе [x] [year], а мы не продаем сигареты несовершеннолетним”
# если пользователю больше 65 - вывести “Вам уже [x] [year], вы в зоне риска”
# в любом другом случае - вывести “Оденьте маску, вам [x] [year]!”
# Пользователь ввел значение возраста [x], на место [year]
# нужно поставить правильный падеж существительного "год", который зависит от значения x. Например:
#
# Тебе 1 год, где твои мама и папа?
#
# Тебе 3 года, где твои мама и папа?
#
# Тебе 5 лет, где твои мама и папа?


EnterAgeOfUser = int(input("Please write your age: "))
EnterAgeOfUserSecond = EnterAgeOfUser % 10

if EnterAgeOfUser>9 and EnterAgeOfUser<20 or EnterAgeOfUserSecond > 4 or EnterAgeOfUserSecond == 0:
    print(f"{EnterAgeOfUser} Лет")
elif EnterAgeOfUserSecond == 1:
    print(f"{EnterAgeOfUser} Год")
else:
    print(f"{EnterAgeOfUser} Года")
