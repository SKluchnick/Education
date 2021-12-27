from random import randint

# Пишем игру. Программа выбирает из диапазона чисел (пусть для начала будет 1-100)
# случайное число и предлагает пользователю его угадать. Пользователь вводит число.
# Если пользователь не угадал - предлагает пользователю угадать еще раз, пока он не угадает.
# Если угадал - спрашивает хочет ли он повторить игру (Y/N). Если Y - повторить. N - Прекратить
def enterInPrograme(stringer):
    if stringer == 'y':
        return True
    elif stringer == 'n':
        return False
    else:
        string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
        enterInPrograme (string)


def enterNumberInGame ():
    # attempt = countOfAttempt()

    while True:
        try:
            integer = int(input("Please write number in range 0-1 "))
            random = randint(0,1)
            if integer == random:
                string = input("Would you like to play again please write 'y' or 'n'").strip().lower()
                if not enterInPrograme(string):
                    break
        except ValueError:
            print("Please write number in range 0-1 ")

enterNumberInGame()




