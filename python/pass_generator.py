import random as rm

digits = '0123456789'
llet = 'abcdefghijklmnopqrstuvwxyz'
blet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!#$%&*+-=?@^_'
dif_symbols = 'il1Lo0O'
chars = ''
answers = []
s = ''

print('Здравствуйте!')
print('Хотите использовать в своём пароле цифры?')
answers.append(input())

print('Хотите использовать в своём пароле строчные буквы?')
answers.append(input())

print('Хотите использовать в своём пароле заглавные буквы?')
answers.append(input())

print('Включать ли символы: "!#$%&*+-=?@^_" ?')
answers.append(input())

print('Исключать ли неоднозначные символы? (il1Lo0O)')
answers.append(input())

if answers[0] == 'Да':
    s += digits

if answers[1] == 'Да':
    s += llet

if answers[2] == 'Да':
    s += blet

if answers[3] == 'Да':
    s += symbols

if answers[4] == 'Да':
    for i in s:
        if i in 'il1Lo0O':
            continue
        chars += i
else:
    chars += s

print('Введите длину пароля:', end = ' ')
length = int(input())

print('Введите количество паролей:', end = ' ')
num = int(input())

for i in range(num):
    for j in range(length):
        print(rm.choice(chars), end = '')
    print()