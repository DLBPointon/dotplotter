#!/usr/bin/env python

"""
-------------------------------------
             Dot Plotter
-------------------------------------
              By 1836811
-------------------------------------
A script to take two sequences and
return a dot plot which shows the 
similarity between the two.
-------------------------------------
Arguments:
    -file1
    The first input file for the
    script

    -file2
    The second input file for the
    script

Optional Arguments:
    --ascii
    Replaces the text output of the
    inner_dotplot with \\ for
    matches and . for no matches.
-------------------------------------

"""
import sys
import argparse
import textwrap
import numpy as np
import matplotlib.pyplot as plt

def parse_command_args(args=sys.argv[1:]):
    """

    """
    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))
    parser.add_argument('-v', '--version',
                        action = 'version',
                        version = '%(prog)s Alpha 1.0')
    parser.add_argument('-file1',
                        type = str,
                        action = 'store',
                        help = 'The first file for input',
                        required = True)
    parser.add_argument('-file2',
                        type = str,
                        action = 'store',
                        help = 'The first file for input',
                        required = True)
    parser.add_argument('--ascii',
                        action = 'store_true',
                        help = 'Specifying this argument, ')

    op = parser.parse_args(args)
    return op


def main():
    
    op = parse_command_args()
    seq_1, seq_2, header_1, header_2 = loadingfiles(op.file1, op.file2,)
    results_list = inner_dotplot(seq_1, seq_2, op.ascii)
    allplot, lenseq1, lenseq2 = outter_dotplot(results_list, seq_1, seq_2)
    matplot = matplotter(seq_1, seq_2, header_1, header_2)

    print(f'The X axis is: {header_1}')
    print(f'X = {seq_1}')
    print(f'The Y axis is: {header_2}')
    print(f'Y = {seq_2}')
    print(allplot)

def loadingfiles(file1, file2):
    with open(file1, 'r') as file1: 
        lines1 = file1.readlines()
        head_1 = lines1[0]
        seq_1 = lines1[1]

    with open(file2, 'r') as file2:
        lines2 = file2.readlines()
        head_2 = lines2[0]
        seq_2 = lines2[1]

    seq_1 = seq_1.strip()
    seq_2 = seq_2.strip()
    return seq_1, seq_2, head_1, head_2


def inner_dotplot(seq_1, seq_2, ascii = False):
    results_list = []
    for i in seq_1:
        for j in seq_2:
            if i == j:
                if ascii == False:
                    results_list.append(i)
                else:
                    results_list.append('\\')
            else:
                if ascii == False:
                    results_list.append('-')
                else:
                    results_list.append(' ')
        results_list.append(f'|{i}\n')
    # print(results_list)
    return results_list


def outter_dotplot(results_list, seq_1, seq_2):
    lenseq1 = len(seq_1)
    lenseq2 = len(seq_2)
    formatting1 = list('=' * lenseq2 + '|\n')
    results_list = list(seq_2) + formatting1 + results_list
    results_list.insert(lenseq2, '\n')

    #print(results_list)
    allplot = ''.join(results_list)
    return allplot, lenseq1, lenseq2


def matplotter(seq_1, seq_2, head_1, head_2):
    listseq1 = list(seq_1)
    listseq2 = list(seq_2)
    print(listseq1)
    print(listseq2)
    # xvalues = np.array(listseq1)
    # yvalues = np.array(listseq2)
    # X,Y = np.meshgrid(xvalues, yvalues)
    # print(X)
    # print(Y)

    # plt.title(f'A Dot-Plot to show the relatedness of {head_1} and {head_2}')
    # plt.xlabel(head_1)
    # plt.ylabel(head_2)
    # plt.show()


if __name__ == '__main__':
    main()
