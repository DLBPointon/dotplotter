#!/usr/bin/env python

""" Please use ./basics.py -h for the full
__doc__ (Not placed here due to Error in calling
__doc__ from textwrap when used in conjunction
with sanity checkers)."""

import sys
if sys.version_info[0] < 3 and sys.version_info[1] < 7:
    raise Exception("""Must be using Python 3.7 for the full
                    functionality of this script""")
if sys.version_info[0] >= 3 and sys.version_info[1] >= 7:
    print('Your using at least Version 3.7, You are good to go...')

PRINT_ERROR = '''Does not exist\n
                 Get module installed before import attempt\n
                 If running server side then contact your admin'''
try:
    import argparse
    print('argparse imported')
except ImportError:
    print('argparse not imported')
    print(PRINT_ERROR)
    sys.exit(0)

try:
    import numpy as np
    print('numpy imported')
except ImportError:
    print('numpy not imported is it installed?')
    print(PRINT_ERROR)
    sys.exit(0)

try:
    import matplotlib.pyplot as plt
    print('matplotlib imported')
except ImportError:
    print('matplotlib not imported is it installed?')
    print(PRINT_ERROR)
    sys.exit(0)

try:
    import os
    print('os imported')
except ImportError:
    print('os not imported is it installed?')
    print(PRINT_ERROR)
    sys.exit(0)

DOCSTRING = """
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
CHECK FOR FOLLOWING DEPENDENCIES:
    - sys - version checking.
    - argparse - command structure.
    - numpy - for matplotlib.
    - matplotlib - graphical plots.
    - os - for directory
           manipulation.

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
    Replaces the ASCII output of the
    inner_dotplot with the Alphabet
    for matches.

    --matplot
    Replaces the terminal output
    with a matplotlib plot.

    --save
    Activates the save function which
    will allow the saving of the
    raw or code plot.
    If used with --matplot, None will
    be saved.
-------------------------------------
Calling this script:

For a basic (ASCII) dotplot you call:
./bascis.py -fasta1 {file1} -fasta2
{file2}

For an Alphabetical plot:
./basics.py -fasta1 {file1} -fasta2
{file2} --code
This will return an alphabetical plot

For a Matplot enabled plot:
./basics.py -fasta1 {file1} -fasta2
{file2} --matplot

Saving files can be called by:
./basics.py -fasta1 {file1} -fasta2
{file2} --code --save {name}
or
./bascis.py -fasta1 {file1} -fasta2
{file2} --save {name}

Saved files will be found in a
dot_plot_output/ folder in the
current directory.
This will contain the user-named
file.
-------------------------------------
"""


def parse_command_args(args=None):
    """ A function to verify arguments and return those
    celled to the required functions.
    args = None means that if nothing is passes then
    sys.argv[1:] is passed"""

    descformat = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog='FileParsing',
                                     formatter_class=descformat,
                                     description=DOCSTRING)

    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s Alpha 1.0')

    parser.add_argument('-fasta1',
                        type=str,
                        action='store',
                        help='The first file for input',
                        required=True,
                        dest='f1')

    parser.add_argument('--fasta2',
                        type=str,
                        action='store',
                        help='The first file for input',
                        dest='f2')

    parser.add_argument('--code',
                        action='store_true',
                        help='''This argument converts code (ascii) to
                        the alphabet''')

    parser.add_argument('--matplot',
                        action='store_true',
                        help='''Converts the traditional Dotplot into a
                         matplot based plot''')

    parser.add_argument('--save',
                        action='store',
                        help='''The file name of the newfile which will
                        contain the output of this script''')

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
        # results_list = codedplot(results_list, lenseq1)
        # Above functio has been cut due to lack of operation

        theplot = outter_dotplot(results_list, seq_1, seq_2, head_1, head_2)
        if option.save:
            saveoutput(theplot, option.save)

    else:
        theplot = outter_dotplot(results_list, seq_1, seq_2, head_1, head_2)

    if option.matplot:
        matplotter(lenseq1, lenseq2)
    else:
        print(theplot)


def loadingfiles(fasta1, fasta2):
    """ A function to take the file paths input
    from the command line and parses the files
    for further use. """
    option = parse_command_args()
    if option.f2:
        print('Two files passed')
        pass
    else:
        print('One file passed \n fasta1 will be used instead')
        fasta2 = fasta1

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
    """ A function which creates the inner plot of the Dotplot in the
    form of a list and also appends the seq to the side of the finished
    plot. If the argument is passed, letters will be replaced with back
    slashes ('\\'). """

    results_list = []
    for i in seq_1:
        for j in seq_2:
            if i == j:
                if code is True:
                    results_list.append(i)

                else:
                    results_list.append('\\')
            else:
                if code is True:
                    results_list.append('-')

                else:
                    results_list.append(' ')
        results_list.append(f'|{i}\n')

    return results_list


def codedplot(results_list, lenseq1):
    """ A function for finding strings of matches and returning
    a '\\' or '.' depending on length of match
    This function was to iterate through the results_list and simply
    replace. This can somewhat work but will not for the last line in 
    the plot."""
    for space in range(len(results_list)):

        if results_list[space] == '\\':

            if results_list[space+lenseq1] == ' ':

                if results_list[space-lenseq1] == ' ':
                    results_list[space-lenseq1] = '.'

                else:
                    results_list[space] = results_list[space]
        else:
            results_list[space] = results_list[space]

        result = ''.join(results_list)
        print(result)


def outter_dotplot(results_list, seq_1, seq_2, head_1, head_2):
    """ A funxction to which finihses the formatting
    of the dotplot and adds the top seq. """

    lenseq2 = len(seq_2)
    formatting1 = list('=' * lenseq2 + '|\n')
    results_list = list(seq_2) + formatting1 + results_list
    results_list.insert(lenseq2, '\n')

    allplot = ''.join(results_list)

    theplot = f'''
The X axis is: {head_1}X = {seq_1}
The Y axis is: {head_2}Y = {seq_2}

{allplot}'''

    return theplot


def matplotter(lenseq1, lenseq2):
    """ A function to convert the results of the previous
    dot plot functions and produce a matplotlib plot
    which conveys the same information in a prettier
    format.
    Duplication of loadingfiles() required for pylint too
    many arguments error."""
    option = parse_command_args()
    seq_1, seq_2, head_1, head_2 = loadingfiles(option.f1, option.f2)

    xvalues = np.array(list(seq_1))
    yvalues = np.array(list(seq_2))

    plt.xticks(np.arange(lenseq1), seq_1)
    plt.yticks(np.arange(lenseq2), seq_2)

    plt.title(f'A Dot-Plot to show the relatedness of\n{head_1}\n&\n{head_2}')

    plt.xlabel(head_1)
    plt.ylabel(head_2)

    plt.imshow(xvalues == yvalues[:, None])
    matplot = plt.show()

    return matplot


def saveoutput(inputed, saved):
    """ A function to add file save functionality"""
    try:
        os.mkdir('dot_plot_output/')
        print('Folder Made')

    except FileExistsError:
        print('Folder already exists')

    with open(f'dot_plot_output/{saved}.txt', 'w') as newfile:
        newfile.write(f'{inputed}')
        print(f'Find your file at {saved}.txt')


if __name__ == '__main__':
    main()
