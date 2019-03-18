#!/user/bin/env python3 -tt
"""
Module documentation.
"""

# Imports
import sys

from app import models


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--flags options] [inputs] ')
        # sys.exit(1)

    models.DataBase.create_it()


# Main body
if __name__ == '__main__':
    main()

# from https://gist.github.com/Abizern/857540/056c4322865b253e72f4ffe697801b8f/
# f09c9bed
