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
The plot can be further modified by
calling the --code and --matplot
flags.
-------------------------------------
Arguments:
    -fasta1
    The first input file for the
    script

    -fasta2
    The second input file for the
    script

Optional Arguments:
    --code
    Replaces the text output of the
    inner_dotplot with \\ for
    matches and . for no matches.

    --matplot
    Replaces the terminal output
    with a matplotlib plot
-------------------------------------

"""
import argparse
import textwrap
import numpy as np
import matplotlib.pyplot as plt


def parse_command_args(args=None):
    """ A function to verify arguments and return those
    celled to the required functions.
    args = None means that if nothing is passes then
    sys.argv[1:] is passed"""

    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=textwrap.dedent(__doc__))

    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s Alpha 1.0')

    parser.add_argument('-fasta1',
                        type=str,
                        action='store',
                        help='The first file for input',
                        required=True,
                        dest='f1')

    parser.add_argument('-fasta2',
                        type=str,
                        action='store',
                        help='The first file for input',
                        required=True,
                        dest='f2')

    parser.add_argument('--code',
                        action='store_true',
                        help='''Specifying this argument converts the
                        letter based output to \\''')

    parser.add_argument('--matplot',
                        action='store_true',
                        help='''Converts the traditional Dotplot into a
                         matplot based plot''')

    option = parser.parse_args(args)
    return option


def main():
    """ The main function which contains all the
    required logic for the correct running of
    the script. """

    option = parse_command_args()
    seq_1, seq_2, head_1, head_2 = loadingfiles(option.f1, option.f2)

    lenseq1 = len(seq_1)
    lenseq2 = len(seq_2)
    
    results_list = inner_dotplot(seq_1, seq_2, option.code)
    
    if option.code:
        results_list = codedplot(results_list, lenseq1)
        allplot = outter_dotplot(results_list, seq_1, seq_2)
    else:
        allplot = outter_dotplot(results_list, seq_1, seq_2)

    if option.matplot:
        matplotter(lenseq1, lenseq2)
    else:
        print(f'The X axis is: {head_1}')
        print(f'X = {seq_1} \n')
        print(f'The Y axis is: {head_2}')
        print(f'Y = {seq_2} \n')
    
    print(allplot)


def loadingfiles(fasta1, fasta2):
    """ A function to take the file paths input
    from the command line and parses the files
    for further use. """

    with open(fasta1, 'r') as fasta1:
        lines1 = fasta1.readlines()
        head_1 = lines1[0]
        seq_1 = lines1[1]

    with open(fasta2, 'r') as fasta2:
        lines2 = fasta2.readlines()
        head_2 = lines2[0]
        seq_2 = lines2[1]

    seq_1 = seq_1.strip()
    seq_2 = seq_2.strip()
    return seq_1, seq_2, head_1, head_2


def inner_dotplot(seq_1, seq_2, code=False):
    """ A function which creates the inner plot of the
    Dotplot in the form of a list and also appends the
    seq to the side of the finished plot.
    if code argument is passed, letters will be replaced with
    back slashes ('\\'). """

    results_list = []
    for i in seq_1:
        for j in seq_2:
            if i == j:
                if code is False:
                    results_list.append(i)
                else:
                    results_list.append('\\')
            else:
                if code is False:
                    results_list.append('-')
                else:
                    results_list.append(' ')
        results_list.append(f'|{i}\n')
    # print(results_list)
    # print(seq_1)
    # print(seq_2)
    return results_list

def codedplot(results_list, lenseq1):
    for slsh in range(len(results_list)):
        if results_list[slsh] == '\\':
            if results_list[slsh+lenseq1] == ' ':
                if results_list[slsh-lenseq1]==' ':
                    results_list[slsh] = '.'
                else:
                    results_list[slsh] = results_list[slsh]
        else:
            results_list[slsh] = results_list[slsh]
        result = ''.join(results_list)
        print(result)


def outter_dotplot(results_list, seq_1, seq_2):
    """ A funxction to which finihses the formatting
    of the dotplot and adds the top seq. """

    lenseq1 = len(seq_1)
    lenseq2 = len(seq_2)
    formatting1 = list('=' * lenseq2 + '|\n')
    results_list = list(seq_2) + formatting1 + results_list
    results_list.insert(lenseq2, '\n')

    allplot = ''.join(results_list)
    # print(allplot)
    return allplot


def matplotter(lenseq1, lenseq2):
    """ A function to convert the results of the previous
    dot plot functions and produce a matplotlib plot
    which conveys the same information in a prettier
    format.
    duplication of loading file required for pylint too
    many arguments error."""
    option = parse_command_args()
    seq_1, seq_2, head_1, head_2 = loadingfiles(option.f1, option.f2)

    xvalues = np.array(list(seq_1))
    yvalues = np.array(list(seq_2))

    plt.xticks(np.arange(lenseq1), seq_1)
    plt.yticks(np.arange(lenseq2), seq_2)

    plt.title(f'A Dot-Plot to show the relatedness of\n{head_1}and\n{head_2}')

    plt.xlabel(head_1)
    plt.ylabel(head_2)

    plt.imshow(xvalues == yvalues[:, None])
    matplot = plt.show()
    return matplot


if __name__ == '__main__':
    main()
