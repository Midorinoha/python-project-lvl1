#!/usr/bin/env python

"""An example script."""

from math import gcd
from random import uniform
from brain_games import questions

def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    name = questions.welcome_user()
    print('Find the greatest common divisor of given numbers.')

    for ir in range(3):
        number = int(uniform(1, 50))
        number1 = number * int(uniform(1, 10))
        number2 = number * int(uniform(1, 10))
        
        ques = str(number1) + ' ' + str(number2)
        answer = questions.question_user(ques)
        correct_answer = gcd(number1, number2)
            
        if answer == str(correct_answer):
            print('Correct!')
            if ir == 2:
                print('Congratulations, {0}!1'.format(name))
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break


if __name__ == '__main__':
    main()
