#!/usr/bin/evn python

"""An example script."""

from random import uniform
from brain_games import questions


def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    name = questions.welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for ir in range(3):
        number = int(uniform(1, 100))
        answer = questions.question_user(number)

        correct_answer = 'no'
        if number % 2 == 0:
            correct_answer = 'yes'

        if answer == correct_answer:
            print('Correct!')
            if ir == 2:
                print('Congratulations, {0}'.format(name))
        else:
            print("'{0}' is wrong answer :(. Correct answer was '{1}'".format(answer, correct_answer))
            print('Let`s try again, {0}'.format(name))
            break


if __name__ == '__main__':
    main()
