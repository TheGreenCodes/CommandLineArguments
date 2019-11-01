import sys

def main(number):
    """Return the square of the number """
    return number* number

number = int(sys.argv[1])

print(main(number))