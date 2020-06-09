"""My Advanced Calculator v1.0

Usage:
  my_calculator.py add (<number><number>)...
  my_calculator.py mult (<number><number>)...
  my_calculator.py square [--verbose] <number>
  my_calculator.py root <number>
  my_calculator.py (-h | --help)
  my_calculator.py --version

Examples:
  my_calculator.py add 9 4 67 101
  my_calculator.py mult 88 43 20458 1 134 
  my_calculator.py square --verbose 9 

Options:
  -h --help        Show this screen.
  -v --version     Show version.
     --verbose         Show details verbosly.

"""

import math
from docopt import docopt


class MyCalculator:
    def get_options(self):
        self.args = docopt(__doc__)

        if self.args["add"]:
            self.addition()
        elif self.args["mult"]:
            self.multiply()
        elif self.args["square"]:
            self.get_square()
        else:
            self.get_root()

    def addition(self):
        """
        Get the summ of all numbers passed
        """
        summation = sum([int(number) for number in self.args["<number><number>"]])
        print(f"{summation}")

    def multiply(self):
        """Get the product of the list of numbers"""
        product = math.prod([int(number) for number in self.args["<number><number>"]])
        print(f"{product}")

    def get_square(self):
        number = int(self.args["<number>"])
        if self.args["--verbose"]:
            print(f"{number} * {number} = {number*number}")
        else:
            print(f"{number*number}")

    def get_root(self):
        """
      Get the square root
      """
        number = self.args["<number>"]
        print(f"{math.sqrt(int(number))}")


if __name__ == "__main__":
    arguments = docopt(__doc__, help=False, version="MyCalculator 1.0")
    calculator = MyCalculator()
    calculator.get_options()
