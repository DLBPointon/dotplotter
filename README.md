[![Build Status](https://travis-ci.com/ARU-Bioinf-IBDS/coursework-DLBPointon.svg?token=LGoasuVQ9cynU6b8TsHk&branch=master)](https://travis-ci.com/ARU-Bioinf-IBDS/coursework-DLBPointon)

# Coursework

## Script to use is basics.py
### Usage:
For a basic ASCII dot plot.
./basics.py -fasta1 {filename} --fasta2 {filename if different from fasta1} 

For an Alphabetical plot:
./basics.py -fasta1 {file1} --fasta2
{file2} --code

For a Matplot enabled plot:
./basics.py -fasta1 {file1} --fasta2
{file2} --matplot

Saving files can be called by:
./basics.py -fasta1 {file1} --fasta2
{file2} --code --save {name}
or
./bascis.py -fasta1 {file1} --fasta2
{file2} --save {name}

## Advanced Features
- Travis CI - implemented 16/12/19 along with badge.
- Matplotlib - implemented 11/12/19.
- Save Function - for raw and code functions implimented 17/12/19.
- Inverted the ASCII and Alphabetical selection - ASCII is default and code arg returns an alphabetised plot.
- Will accept only one file, this will be used as both sequences.
