#!/usr/bin/env python

"""Main file of brain-games."""

from brain_games import cli


def main():
    """Show welcome message."""
    print('Welcome to the Brain Games!')  # noqa:WPS421
    cli.welcome_user()


if __name__ == '__main__':
    main()
