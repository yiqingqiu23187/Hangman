'''
hangmanlib.py
   A set of library functions for use with your Hangman game
   Actually you can add all help functions here, and just 
   import you can use all functions! 
   Enjoy!
'''
import random
import csv
import datetime

LINEPERIMAGE = 9  # Every LINEPERIMAGE is a perfect picture of hangman
SPACENNUM = 30

start_time = datetime.datetime.now()
user_input = ''
mistakes = 0
real_word = ''
guess_word = ''


def print_hangman(message, mistakes=6):
    '''
    print hangman : from 0 (hang) to 6 (hanged)
    '''

    lines = LINES.split('\n')
    start = mistakes * LINEPERIMAGE
    for i in range(LINEPERIMAGE):
        if i != LINEPERIMAGE // 2:
            print(' ' * SPACENNUM + lines[start + i])
        else:
            left = (SPACENNUM - len(message)) // 2
            print(' ' * left + message + ' ' * (SPACENNUM - left - len(message)) + lines[start + i])


# end print_hangman_image

# We intentionally add LINES below: it's too long
LINES = ''' ______
|  |
|  
| 
|  
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| 
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /
|  
| 
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
|  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| /  
|_____
|     |____
|__________|
 ______
|  |
|  O
| /|\ 
|  |
| / \ 
|_____
|     |____
|__________|

'''


def init():
    global real_word, guess_word, mistakes, start_time, user_input
    start_time = datetime.datetime.now()
    user_input = ''
    mistakes = 0
    with open("./words.txt", "r") as file:
        data = file.read().split()
        real_word = random.choice(data)
        guess_word = '_ ' * len(real_word)


def calculate(letter):
    global real_word, guess_word, mistakes
    if letter in real_word:
        for i in range(len(real_word)):
            if real_word[i] == letter:
                guess_word = guess_word[:2 * i] + letter + guess_word[2 * i + 1:]
    else:
        mistakes += 1


def save_result():
    time_span = (datetime.datetime.now() - start_time).total_seconds()
    with open(r'./guess.csv', mode='a', newline='', encoding='utf8') as cfa:
        wf = csv.writer(cfa)
        # 写入游戏开始的时间,单次游戏使用的时间,猜测的单词,用户猜测的字符序列
        data2 = [[start_time, str(time_span) + '秒', real_word, user_input]]
        for i in data2:
            wf.writerow(i)
    letter = input('Continue game(C[c]/Q[q])? ')
    while (len(letter) != 1 or (letter != 'c' and letter != 'C' and letter != 'Q' and letter != 'q')):
        letter = input('just press one letter: C[c]/Q[q]: ')
    return letter


if __name__ == '__main__':
    letter = 'c'
    while letter == 'c' or letter == 'C':
        init()
        while mistakes < 6:
            print_hangman(guess_word, mistakes)

            letter = input()
            while len(letter) != 1 or not 'a' <= letter <= 'z':
                letter = input('just press one letter from a to z, try again: ')
            user_input += letter

            calculate(letter)

            if mistakes == 6:
                print_hangman('YOU LOSE!', mistakes)
                print('The secret word is %s, you guess via sequence %s. And YOU LOSE!' % (real_word, user_input))
                letter = save_result()
            elif '_' not in guess_word:
                print_hangman('YOU WIN!', mistakes)
                print('The secret word is %s, you guess via sequence %s. And YOU WIN!' % (real_word, user_input))
                letter = save_result()
                break
