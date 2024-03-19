#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pythontemplate.py
#
"""
pythontemplate.py is a template that includes argparse.ArgumentParser-style
arguments in all their various forms.
"""

__author__ = "David C. Petty"
__copyright__ = "Copyright 2020, David C. Petty"
__license__ = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
__version__ = "0.0.2"
__maintainer__ = "David C. Petty"
__email__ = "david_petty@psbma.org"
__status__ = "Hack"

import argparse, os, sys


class Parser(argparse.ArgumentParser):
    """Create OptionParser to parse command-line options."""
    def __init__(self, **kargs):
        argparse.ArgumentParser.__init__(self, **kargs)
        # self.remove_argument("-h")
        self.add_argument("-?", "--help", action="help",
                          help="show this help message and exit")
        self.add_argument('--version', action='version',
                          version=f"%(prog)s {__version__}")

    def error(self, msg):
        sys.stderr.write("%s: error: %s\n\n" % (self.prog, msg, ))
        self.print_help()
        sys.exit(2)


def main(argv):
    """This is a template that includes OptionParser-style arguments."""
    description = """This is a template that includes 
    argparse.ArgumentParser-style arguments in all their various forms."""
    formatter = lambda prog: \
        argparse.ArgumentDefaultsHelpFormatter(prog, max_help_position=30)
    parser = Parser(description=description, add_help=False,
                    formatter_class=formatter)
    arguments = [
        # c1, c2, action, dest, default, help
        ('-a', '--arg', 'store', 'ARG', None, 'argument \u2014 multiples supersede', ),
        ('-m', '--mult', 'append', 'MULT', None, 'multi-argument  \u2014 multiples accumulate', ),
        ('-v', '--verbose', 'store_true', 'VERBOSE', False,
         'echo status information', ),
    ]
    # Add optional arguments with values.
    for c1, c2, a, v, d, h in arguments:
        parser.add_argument(c1, c2, action=a, dest=v, default=d, help=h,)
    # Add positional arguments. 'NAME' is both the string and the variable.
    parser.add_argument("REQUIRED", help="required argument")
    parser.add_argument("OPTIONAL", nargs="*", help="optional arguments")
    # Parse arguments.
    pa = parser.parse_args(args=argv[1: ])
    if pa.ARG:
        os.environ['ARG'] = pa.ARG
        print(f"ARG = {pa.ARG}")
    if pa.MULT:
        print(f"MULT= {pa.MULT}")
    if pa.REQUIRED:
        print(f"REQ = {pa.REQUIRED}")
    if pa.OPTIONAL:
        print(f"OPT = {pa.OPTIONAL}")


if __name__ == '__main__':
    is_idle, is_pycharm, is_jupyter = (
        'idlelib' in sys.modules,
        int(os.getenv('PYCHARM', 0)),
        '__file__' not in globals()
    )
    if any((is_idle, is_pycharm, is_jupyter,)):
        tests = [
            ['template.py', 'REQ', ],
            ['template.py', 'REQ', 'OPT1', ],
            ['template.py', 'REQ', 'OPT1', 'OPT2', 'OPT3',
             '-a', 'FOO', '-m', 'MULT1', '-m', 'MULT2', ],
            ['template.py',
             '-a', 'BAR', '-m', 'MULT1', '-m', 'MULT2',
             'REQ', 'OPT1', 'OPT2', 'OPT3', ],
            ['template.py', '-?', ],
        ]
        for test in tests:
            print(f"# {' '.join(test)}")
            main(test)
            print()
    else:
        main(sys.argv)
