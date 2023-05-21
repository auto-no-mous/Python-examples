import json
import random

def screen(s):
    s = s.upper()
    s = list(s)
    s = '| ' + '   '.join(s) + ' | '
    print('-' * len(s))
    print(s)
    print('-' * len(s))


def victory(word, attempts):
    print('ПРАВИЛЬНО!')
    diff = len(word)-attempts
    if diff == 0:
        print('Это действительно \"{0}\", и вы угадали это с ПЕРВОЙ ПОПЫТКИ! Невероятно!'.format(word))
    elif diff == 1:
        print('Это действительно \"{0}\", и вы угадали это со второй попытки! Отлично!'.format(word))
    else:
        print("Это действительно \"{0}\", и вы угадали это, потратив попыток: {1}".format(word, diff))


def load_words():
    with open('words.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    words = list(text['quest'])
    random.shuffle(words)
    return words

filler = '?'
print("Добро пожаловать на 'Поле Чудес!'".upper())
print('===============ЖЕЛАЕМ УДАЧИ!=================')
words = load_words()
while len(words) > 0:
    current = words.pop()
    quest = filler * len(current['word'])
    attempts = len(current['word'])
    print('\nВы можете угадывать по одной букве, или написать сразу ответ')

    while attempts > 0:
        print("Попыткок, чтобы угадать загаданное слово: {0}".format(attempts))
        print(current['tip1'])
        screen(quest)
        answer = input().lower()
        if answer == current['word']:
            victory(answer, attempts)
            break
        elif len(answer) == 1:
            if answer in current['word']:
                quest = list(quest)
                pos = current['word'].find(answer)
                count = 0
                while pos != -1:
                    quest[pos] = current['word'][pos]
                    count += 1
                    if pos != len(current['word']) - 1:
                        pos = current['word'].find(answer, pos + 1)
                    else:
                        break
                if count > 1:
                    print('Вот это удача, букв открыто: {0}'.format(count))
                else:
                    print('Отлично, вы открыли букву!')
                quest = ''.join(quest)
                if filler not in quest:
                    victory(quest, attempts)
            else:
                print('Такой буквы в слове нет.')
            attempts -= 1
        else:
            print('Неудача, это вовсе не ' + answer)
            attempts = 0
    print('Было загадано слово: ' + current['word'].upper())
    print('===============КОНЕЦ РАУНДА=================')
    i = input('1 - продолжить, 2 - выход: ')
    if i == '2':
        break
    else:
        continue

print('Игра окончена')
