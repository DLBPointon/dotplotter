#!/usr/bin/env python

"""
-------------------------------------------------------------
                Welcome to Dot-Plotter
-------------------------------------------------------------
This program is written to take 2 input files (FASTA format)
and return a text file with a ACSII or Matplotlib.pyplot plot
-------------------------------------------------------------
            Two File inputs will be required
-------------------------------------------------------------

"""

import argparse
import textwrap
import sys


def parse_command_args(args=sys.argv[1:]):
    """
    Sets up and parses command line arguments

    Returns:
        the arguments namespace
    """
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='Dot-Plotter',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))
    parser.add_argument('-file1', '--File1',
                        type=str,
                        action='store',
                        help='Input first FASTA file',
                        dest="f1",
                        required=True)
    parser.add_argument('-file2', '--File2',
                        type=str,
                        action='store',
                        help='Input Second FASTA file',
                        dest="f2",
                        required=True)
    parser.add_argument('-out', '--outfile',
                        action='store',
                        help='Location of out')
    parser.add_argument('-filter',
                        action='store_false',
                        help='Arg will produce a simlified ACSII graph',
                        dest='fil')
    parser.add_argument('-ascii',
                        action='store_false',
                        help='Arg will produce an ASCII graph',
                        dest='asc')
    parser.add_argument('-matplot',
                        action='store_false',
                        help='Arg will produce a Matplotlib graph',
                        dest='plot')

    arguments = parser.parse_args(args)
    return arguments


def main():
    """
    This function checks for args and calls functions
    """
    options = parse_command_args()
    af1 = sys.argv[2]
    af2 = sys.argv[4]
    for arg in sys.argv:
        print(arg)

        if arg == file1 and file2 and out:
            dotplotter(af1, af2, sys.argv[6])


def dotplotter(file1, file2, out):
    """The main function which contains all of the logic used in this script"""
    print('well done')


def asciitoggle():
    """This sub-function when True will create an ascii table for readability"""
    print('Activate ASCII')


def matplottoggle():
    """This sub-funtion will create a matplotlib graph showing a
    graph with a high level of readability"""
    print('Activate Matplotlib')


def filtertoggle():
    """This sub-function will create an ASCII table with a simplified legend"""
    print('Activate Simple View')


# End of FILE
if __name__ == '__main__':
    main()
