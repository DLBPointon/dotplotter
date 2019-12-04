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
import matplotlib.pyplot as plt
import numpy as np


def parse_command_args(args=sys.argv[1:]):
    """
    Sets up and parses command line options

    Returns:
        the options namespace
    """
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='Dot-Plotter',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))
    parser.add_argument('file1',
                        type=str,
                        action='store',
                        help='Input first FASTA file',
                        dest="f1",
                        required=True)
    parser.add_argument('file2',
                        type=str,
                        action='store',
                        help='Input Second FASTA file',
                        dest="f2",
                        required=True)
    parser.add_argument('-out',
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
    parser.add_argument('-w', '--window',
                        action='store',
                        type=int,
                        help='''Arg will specify the about of sequence
                        to compare if more than 20bp''')

    options = parser.parse_args(args)
    return options


def main():
    """
    This function checks for args and calls functions
    """
    options = parse_command_args()
    af1 = options.f1
    af2 = options.f2
    if options.f1 and options.f2:
        dotplotter(af1, af2)
    else:
        print('You havent entered the correct options')
        sys.exit(0)


def openandsort(file1, file2):
    with open(file1, 'r') as sequence1:
        lines1 = sequence1.readlines()
        seq1 = lines1[1]
        head1 = lines1[0]

    with open(file2, 'r') as sequence2:
        lines2 = sequence2.readlines()
        seq2 = lines2[1]
        head2 = lines2[0]

    return seq1, head1, seq2, head2


def asciitoggle():
    """This sub-function when True will create an ascii
    table for readability"""
    print('Activate ASCII')


def matplottoggle():
    """This sub-funtion will create a matplotlib graph showing a
    graph with a high level of readability"""
    print('Activate Matplotlib')


def filtertoggle():
    """This sub-function will create an ASCII table with a simplified legend"""
    print('Activate Simple View')
    # replace \\ with letter thats matched.


def marker(seq1, seq2):
    """A sub-function which marks the 
    points where the sequences are similar"""
    if seq1 == seq2:
        return 0
    else:
        return 1


def matrixspace(seq1, seq2, window, i=0, j=0):
    """A sub-function to create the matrix space, 
    now iterating over the sequences independantly * window 
    we move through and check where there are similarities,
    makes a list of scores"""
    iterseq1 = seq1[i:i+window]
    iterseq2 = seq2[j:j+window]

    print(iterseq1)
    print(iterseq2)

    zipped = zip(iterseq1, iterseq2)
    for x, y in zipped:
        return marker(x, y)


def makematrix(seq1, seq2):
    """A sub-function to create the matrix shape"""
    lenseq1 = len(seq1)
    lenseq2 = len(seq2)

    range1 = range(lenseq1)
    range2 = range(lenseq2)
    #
    for i in range1:
        for j in range2:
            return i, j

def plotmatrix(matrix, thresh, seq1, seq2):
    """A sub-function to plot the results onto the matrix"""
    notblank = '\\'
    blank = ' '
    line = ''

    for i in seq2:
            for j in seq1:
                if i == j:
                    line = ''.join(notblank)
                else:
                    line = ''.join(blank)

    print('\\|' + seq2)
    print('-' * len(seq1) + '--')
    for letter in seq1:
        print(f'{letter}|{line}')


def dotplotter(af1, af2, window = 1, thresh = 1):
    """The main function which contains all of the logic used in this script"""
    options = parse_command_args()
    seq1, head1, seq2, head2 = openandsort(af1, af2)
    matrix = matrixspace(seq1, seq2, 0, 0, window)
    print(matrix)
    print(marker(seq1, seq2))
    plotmatrix(matrix, thresh, seq1, seq2)
    
    print(seq1)
    print(seq2)
 
    seq11 = []
    seq22 = []
    for i in seq1:
        seq11.append(i)
    print(seq11)
    for j in seq2:
        seq22.append(j)
    print(seq22)
    x = np.array(seq11, seq22)

# End of FILE
if __name__ == '__main__':
    main()
