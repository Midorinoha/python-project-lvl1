#!/usr/bin/env python

"""An example script."""

#from prompt import string
from random import uniform
from brain_games import questions

def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    name = questions.welcome_user()
    print('What is the result of the expression?')

    for ir in range(3):
        number1 = int(uniform(1, 100))
        number2 = int(uniform(1, 100))
        
        if ir == 0:
            ques = str(number1) + '+' + str(number2)
            answer = questions.question_user(ques)
            correct_answer = number1 + number2
        elif ir == 1:
            ques = str(number1) + '-' + str(number2)
            answer = questions.question_user(ques)
            correct_answer = number1 - number2
        else:
            ques = str(number1) + '*' + str(number2)
            answer = questions.question_user(ques)
            correct_answer = number1 * number2
            
        if answer == str(correct_answer):
            print('Correct!')
            if ir == 2:
                print('Congratulations, {0}!'.format(name))
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
            print("Let's try again, {0}!".format(name))
            break


if __name__ == '__main__':
    main()
