import random as rm

list_of_words = ['дерево', 'дом', 'камень', 'школа', 'университет', 'арбуз', 'автобус', 'цирк', 'дружба', 'нога', 'рука', 'серый', 'волк', 'жёлтый', 'север', 'дискриминант', 'бесконечность', 'машина', 'орёл', 'медведь', 'рог', 'серебро', 'золото', 'кольцо', 'монета']

def get_word():
    return rm.choice(list_of_words)

def answer():
    if input().lower() == 'да':
        return True

    else:
        return False
        
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play():

    tries = 6
    print('Давайте сыграем в угадайку!')

    guessed_letters = []
    s = ''
    i = 0

    word = get_word()

    for j in range(len(word)):
        print('_', end = ' ')

    print()

    while True:
        s += input()
        if s.index(s[i]) != i:
            print('Вы уже вводили эту букву')
            i += 1
            continue
        if s[i] in word:
            guessed_letters.append(s[i])
            i += 1
            counter = 0
            for j in range(len(word)):
                if word[j] in guessed_letters:
                    print(word[j], end = ' ')

                else:
                    print('_', end = ' ')
                    counter += 1
            print()

            if counter == 0:
                print('Вы выиграли!')
                break

        else:
            i += 1
            for j in range(len(word)):
                if word[j] in guessed_letters:
                    print(word[j], end = ' ')

                else:
                    print('_', end = ' ')

            print()
            
            print(display_hangman(tries))
            tries -= 1
        if tries == -1:
            print('Вы проиграли. Правильное слово: ', word)
            break
    
print('Хотите сыграть?')

answ = answer()

if answ == True:
    play()

else:
    print('Как хотите')

while answ == True:
    print('Хотите сыграть ещё раз?')

    if answer() == True:
        play()

    else:
        print('До свидания!')
        break

        
        