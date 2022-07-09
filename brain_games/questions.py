"""Interactiv with user."""

from cgitb import text
from prompt import string


def welcome_user():
    """Hello user."""
    name = string('May I have your name? ')
    print('Hello, {0}'.format(name))
    return name

def question_user(ques) -> str:
    """Ask a user a question."""
    if type(ques) is list:
        text = ''
        for i in ques:
            text += str(i) + ' '
        ques = text
    answer = string('Question: {0}? '.format(ques))
    print('Your answer: {0}'.format(answer))
    return answer
    
