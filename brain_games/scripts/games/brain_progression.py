#!/usr/bin/env python

"""An example script."""

from random import uniform
from brain_games import questions

def main():
    """Run an example code."""
    print('Welcome to the Brain Games!')
    name = questions.welcome_user()
    print('What number is missing in the progression?')

    for ir in range(3):
        next_number = int(uniform(1, 10))
        num_increase = int(uniform(1, 10))
        num_list = []
        hidden_number = int(uniform(0,10))
        print(hidden_number)
        correct_answer = ''
        for i in range(10):
            if i == hidden_number:
                correct_answer = str(next_number)
                num_list.append('..')
            else: 
                num_list.append(str(next_number))
            next_number += num_increase
        
        answer = questions.question_user(num_list)
            
        if answer == correct_answer:
            print('Correct!')
            if ir == 2:
                print('Congratulations, {0}'.format(name))
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(answer, correct_answer))
            print('Let`s try again, {0}'.format(name))
            break


if __name__ == '__main__':
    main()
