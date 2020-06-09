"""My Advanced Calculator.

Usage:
  my_calculator.py add <number><number>... 
  my_calculator.py mult <number><number>...
  my_calculator.py square <number> 
  my_calculator.py (-h | --help)
  my_calculator.py --version

Arguments:


Options:
  -a --add         Get the sum of two or more numbers 
  -m --mult        Get the product of two or more numbers
  --square         Get the square of a number
  --root           Get the square root of a number
  -h --help        Show this screen.
  -v --version     Show version.

"""
from docopt import docopt
from schema import Schema, And, Optional, Or, Use, SchemaError


class MyCalculator:
    def get_options(self):
        self.args = docopt(__doc__)
        print(args)

    def addition(self):
        """
        Get the summ of all numbers passed
        """
        pass


if __name__ == "__main__":
    arguments = docopt(__doc__, version="MyCalculator 1.0")
    prog = MyCalculator()
    prog.get_options()
