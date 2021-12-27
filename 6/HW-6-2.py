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

# rangeOfDigits ()

def countOfAttempt ():
    try:
        numberAttempt = int(input("Please write number of attempts  "))
        return numberAttempt
    except ValueError:
            print("Please write only number ")

# res = countOfAttempt()
# print(res)


def enterNumberInGame ():
    attempt = countOfAttempt()
    print(f'you have {attempt} attempts')
    while True:
        try:

            integer = int(input("Please write number in range 0-1 "))
            attempt -= 1
            print(f'you have {attempt} attempt')
            random = rangeOfDigits()
            if integer == random:
                string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
                if not enterInPrograme(string):
                    break
        except ValueError:
            print("Please write number in range 0-1 ")

enterNumberInGame ()