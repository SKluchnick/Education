from random import randint


# 4. ** Добавить в задание 2 вывод сообщения-подсказки. Если пользователь ввел число, и не угадал - сообщать:
# "Холодно" если разница между загаданным и введенным числами больше 10,
# "Тепло" - если от 5 до 10 и "Горячо" если от 4 до 1.

def enterInPrograme(stringer):
    if stringer == 'y':
        return True
    elif stringer == 'n':
        return False
    else:
        string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
        enterInPrograme(string)


def rangeOfDigits():
    try:
        integerFirst = int(input("Please write start of range  "))
        integerSecond = int(input("Please write start of range  "))
        random = randint(integerFirst, integerSecond)
        print(random)
        return random
    except ValueError:
        print("Please write only number ")


rangeOfDigits ()

def countOfAttempt():
    try:
        numberAttempt = int(input("Please write number of attempts  "))
        return numberAttempt
    except ValueError:
        print("Please write only number ")


res = countOfAttempt()
print(res)

def prediction(numFirst, numSecond):
    string = ''
    if abs(numFirst - numSecond) > 10:
        string = 'Cold'
    if 5 <= abs(numFirst - numSecond) <= 10:
        string = 'Hot'
    if 1 <= abs(numFirst - numSecond) <= 4:
        string = 'Really Hot'
    return string

#
prediction(30, 5)



def enterNumberInGame():
    attempt = countOfAttempt()
    print(f'you have {attempt} attempts')
    while True:
        try:
            integer = int(input("Please write number in range 0-15 "))
            random = rangeOfDigits()
            predict = prediction(integer, random)
            print(predict)
            if integer == random:
                string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
                attempt = countOfAttempt()
                print(f'you have {attempt} attempts')
                if not enterInPrograme(string):
                    break
            else:
                attempt = attempt - 1
                print(f'you have {attempt} attempts')
                if attempt != 0:
                    continue
                else:
                    print("Loser")
                    break
        except ValueError:
            print("Please write number in range 0-15 ")


enterNumberInGame()
