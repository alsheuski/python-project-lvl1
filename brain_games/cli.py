"""CLI module."""
import prompt


def welcome_user():
    """Ask a name of user and greet them."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))  # noqa:WPS421
