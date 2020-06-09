import docopt

"""Naval Fate.

Usage:
  advanced_square.py ship new <name>...
  advanced_square.py ship <name> move <x> <y> [--speed=<kn>]
  advanced_square.py ship shoot <x> <y>
  advanced_square.py mine (set|remove) <x> <y> [--moored | --drifting]
  advanced_square.py (-h | --help)
  advanced_square.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt
import os

# from schema import Schema, And, Optional, Or, Use, SchemaError


class Sim:
    def get_options(self):
        args = docopt(__doc__)
        print(args)
        # schema = Schema(
        #     {
        #         "PARAMFILE": Use(open, error="PARAMFILE should be readable"),
        #         "SPICEDECK": os.path.isfile,
        #         object: object,
        #     }
        # )
        # try:
        #     args = schema.validate(args)
        # except SchemaError as e:
        #     exit(e)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="Naval Fate 2.0")
    # print(arguments)
    # prog = Sim()
    # prog.get_options()
