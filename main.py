import sys
import random
import csv
import datetime
from hangmanlib import print_hangman

start_time = datetime.datetime.now()
time_span = 0
user_input = ''
mistakes = 0
real_word = ''
guess_word = ''


def init():
    global real_word, guess_word, mistakes, start_time, user_input
    print('Welcome to the Hangman game!')
    start_time = datetime.datetime.now()
    user_input = ''
    mistakes = 0
    with open("words.txt", "r") as file:
        data = file.read().split()
        real_word = random.choice(data)
        guess_word = '_ ' * len(real_word)
        print(real_word)
    print('I have generate a word for you, press a-z to guess all its letters')


def print_stage():
    print('Now the word is ' + guess_word)
    print('mistakes:%d' % mistakes)
    print_hangman(mistakes)


def handle_input():
    global user_input
    letter = input('press a-z to guess: ')
    while len(letter) != 1 or not 'a' <= letter <= 'z':
        letter = input('just press one letter from a to z, try again')
    user_input += letter
    return letter


def calculate(letter):
    global real_word, guess_word, mistakes
    if letter in real_word:
        for i in range(len(real_word)):
            if real_word[i] == letter:
                guess_word = guess_word[:2 * i] + letter + guess_word[2 * i + 1:]
    else:
        mistakes += 1


def continue_or_quit():
    global start_time, time_span
    time_span = (datetime.datetime.now() - start_time).total_seconds()
    save_result()
    decision = input('press c to play again and q to quit: ')
    while (len(decision) != 1 or (decision != 'c' and decision != 'q')):
        decision = input('just press one letter:c or q: ')
    if decision == 'c':
        start_one_game()
    else:
        sys.exit(0)


def save_result():
    with open(r'./guess.csv', mode='a', newline='', encoding='utf8') as cfa:
        wf = csv.writer(cfa)
        # 写入游戏开始的时间,单次游戏使用的时间,猜测的单词,用户猜测的字符序列
        data2 = [[start_time, str(time_span) + '秒', real_word, user_input]]
        for i in data2:
            wf.writerow(i)


def check_result():
    if mistakes == 6:
        print_stage()
        print('The word is %s', real_word)
        print('Sorry, you failed the game!')
        continue_or_quit()
    elif '_' not in guess_word:
        print('The word is %s', real_word)
        print('Congratulations! You won the game.')
        continue_or_quit()


def start_one_game():
    init()
    while mistakes < 6:
        print_stage()
        letter = handle_input()
        calculate(letter)
        check_result()


if __name__ == '__main__':
    start_one_game()
