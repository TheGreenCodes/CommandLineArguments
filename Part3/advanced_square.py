import getopt
import sys
from math import sqrt

"""
get the square but get the square root incase the argument 'root' is provided
"""


def usage():
    """
    Show help for the CLI program
    """
    print("python advanced_square.py --number <your_number> \n OR\n")
    print("python advanced_square.py -n <your_number>\n")
    print("To get the square root: python advanced_square.py -n <your_number> -r")
    print("Example: get the square\n\tpython advanced_square.py -n 5")


def main():

    try:
        option, arguments = getopt.getopt(
            sys.argv[1:], "hn:r", ["help", "number=", "root"]
        )
    except getopt.GetoptError as error:
        print(error)
        sys.exit()

    number = None
    root_number = False

    for opt, variable in option:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-n", "--number"):
            number = int(variable)
        elif opt in ("-r", "--root"):
            root_number = True
        else:
            usage()
            sys.exit()

    if root_number:
        print(f"The square root of {number} = {sqrt(number)}")
    else:
        print(f"The square of {number} = {number* number} ")


if __name__ == "__main__":
    main()
