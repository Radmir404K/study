import random as rm

print('Добро пожаловать в числовую угадайку!')

def new_game():
    global n
    n = rm.randint(1, 100)
    global k
    k = 1

def is_valid(num):
    if num < 1 or num > 100:
        return False
    else:
        return True

new_game()

while True:
    attempt = int(input())
    if is_valid(attempt) == False:
        print('А может быть все-таки введем целое число от 1 до 100?')
    else:
        if attempt == n:
            print('Вы угадали, поздравляем!')
            print(k)
            print('Хотите загадать новое число?')
            if input() == 'Да':
                new_game()
                continue
            else:
                break
        elif attempt < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            k += 1
        else:
            print('Ваше число больше загаданного, попробуйте еще разок')
            k += 1