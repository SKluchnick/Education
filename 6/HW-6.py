from random import randint

# * Добавить в задание 2 счетчик попыток и диапазон чисел (начало и конец).
# Пользователь вводит количество попыток, за которые он может угадать число.
# Пользователь вводит начало и конец диапазона. На каждом шаге угадывания числа сообщайте пользователю сколько попыток у него осталось.
# Если пользователь не смог угадать за отведенное количество попыток сообщить ему об окончании (Looser!).
def enterInPrograme(stringer):
    if stringer == 'y':
        return True
    elif stringer == 'n':
        return False
    else:
        string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
        enterInPrograme (string)


def rangeOfDigits ():
    try:
        integerFirst = int(input("Please write start of range  "))
        integerSecond = int(input("Please write start of range  "))
        random = randint(integerFirst, integerSecond )
        print(random)
        return random
    except ValueError:
            print("Please write only number ")

rangeOfDigits ()




