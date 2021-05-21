import random
from hangmanlib import print_hangman

mistakes = 0
real_word = ''
guess_word = ''


def init():
    global real_word, guess_word, mistakes
    print('Welcome to the Hangman game!')
    mistakes = 0
    with open("words.txt", "r") as file:
        data = file.read().split()
        real_word = random.choice(data)
        guess_word = '_ ' * len(real_word)
        print(real_word)
    print('I have generate a word for you, press a-z to guess all its letters')


def print_stage():
    print('Now the word is ' + guess_word)
    print_hangman(mistakes)


def handle_input():
    letter = input('press a-z to guess')
    if len(letter) != 1 or not 'a' <= letter <= 'z':
        print('just press one letter from a to z, try again')
        letter = handle_input()
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
    decision = input('press c to play again and q to quit')
    while (len(decision) != 1 or (decision != 'c' and decision != 'q')):
        decision = input('just press one letter:c or q')
    if decision == 'c':
        start_one_game()
    else:
        SystemExit(0)


def check_result():
    if mistakes == 6:
        print_stage()
        print('Sorry, you failed the game!')
        continue_or_quit()
    elif '_' not in guess_word:
        print('Congratulations! You won the game.')
        print('The word is %s', real_word)
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
