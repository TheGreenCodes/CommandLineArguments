import sys


def main(first_number, second_number):
    """Return the SUM of the number """
    return first_number + second_number


first_number = int(sys.argv[1])
second_number = int(sys.argv[2])

print(main(first_number, second_number))
