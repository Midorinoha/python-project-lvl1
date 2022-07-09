"""Interactiv with user."""

import prompt


def welcome_user():
    """Hello user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
