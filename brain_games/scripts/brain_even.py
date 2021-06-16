"""Brain even script."""

import random
import prompt

from brain_games import cli


def main():
    """Show welcome message."""
    print('Welcome to the Brain Games!')
    username = cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    right_answers_count = 0

    while right_answers_count < 3:
        number = random.randint(0, 100)
        print('Question: {}'.format(number))
        user_answer = prompt.string('Your answer: ')

        if user_answer != 'no' and user_answer != 'yes' or \
                user_answer != correct_answer(number):
            print('\'{}\' is wrong answer ;(. Correct answer was \'{}\'.'.format(
                user_answer, correct_answer(number)))
            print('Let\'s try again, {}!'.format(username))
            break

        print('Correct!')
        right_answers_count += 1

        if right_answers_count == 3:
            print('Congratulations, {}!'.format(username))


def correct_answer(number):
    if is_even(number):
        return 'yes'
    return 'no'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    main()
