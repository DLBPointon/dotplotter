[![Build Status](https://travis-ci.com/ARU-Bioinf-IBDS/coursework-DLBPointon.svg?token=LGoasuVQ9cynU6b8TsHk&branch=master)](https://travis-ci.com/ARU-Bioinf-IBDS/coursework-DLBPointon)

# Coursework-1836811

## Advanced Features
- Travis CI - implemented 16/12/19 along with badge.
- Matplotlib - implemented 11/12/19.
- Save Function - for raw and code functions implimented 17/12/19.
- Inverted the ASCII and Alphabetical selection - ASCII is default and code arg returns an alphabetised plot.
- Will accept only one file, this will be used as both sequences.

## 29/11/19
- Started and outlined use of Argument Parser command structure.
- Started outline of definitions I may need for the script.
- Pycodestyle compliant and pylint score of 3.75 (due to the early nature of the script)
- Arg.Parse structure is reused from personal work found on GitHub-

## 3/12/19
- Added more structure to the script.
- Added more functions.
- Added import statements.
- pycodestyle compliant and pylint score of 5.93.
- Updated from sys.argv to arg.parse options.

## 4/12/19
- Half of the functions now work.
- Structure has been lost and work has become rather 'scatty'.
- There is some duplication of efforts where I have gotten carried away.
### Update 2
- Over complecated structure of dotplot.py has lead me to start again in basics.py.
- basics.py takes input sequences and returns the inner space of a dotplot.
- Double printing of dotplot bug.

## 5/12/19
- Inner_dotplot function working.
- May require the joining of the innerplot to happen after the outter plot is added to the list.
### Update 2
- Dot plotting now works with same and variable length input strings.
- Issues with double printing of plot have been fixed.
### Update 3
- pytest on inner_dotplot function - Passed
- pytest on outter_dotplot function - Fails due to multi-line formatting error
### Update 4
- Basic ArgParse arguments have been set and tested.
- Script is now executable.
- Now takes input files - although function could be halved.
- Tested on various size files and is working.
- ascii filter works when specified as --ascii in the command line.

## 9/12/19
- Added strip to seq_1 and seq_2 to get rid on unexpected newlines.
### Update 2
- Started on Matplotlib implimentation.

## 10/12/19
- Added __doc__ to each function.
- Additional changes to matplot function.

## 11/12/19
- Completed matplot function, this stops the printing of the terminal dotplot and only returns the matplotlib variant called via --matplot.
### Update 2
- PyCodeStyle compliant, formatting fixes and argument syntax fixes.
### Update 3
- argument --ascii has been changed to --code to comply with pylint.
### Update 4
- arguments -file1 and -file2 changed to fasta1 and fasta2.
- loadingfiles function duplicated in matplot function for pylint compliance of too many arguments. Avoiding use of global to ease this as it could complicate code.
- sys.argv[1:] replaced with None.
- removed import sys as now defunc.
- PyLint score of 9.73.
- PyCodeStyle compliant.

## 12/12/19
- PyTest files formatted for PyCodeStyle compliance.
	- Finally Uploaded after not including them along with commits.
	- Test per file due to failing if more than one test is in each file (carrying over of previous test results).
- Recap on PyTests.
	- InnerDotplot tests all pass.
	- OutterDotplot tests all pass.

## 13/12/19
- Started of a propper filter implimentation which will replace singluar matches with '.' rather than '\\'.
- This function works but struggles when it comes to the end of the list - index out of range error.
- Changes to command structure for flexibility of flag usage.

## 16/12/19
- Edited test scripts to the current and correct number of arguments.
- All tests are now in the main folder, as opposed to the test_scripts folder, made for failures in getting script.
- TravisCI implimented and Badge added to the README.md.
- Small additions have been made to basics.py for PyCodeStyle compliance.
- PyCodeStyle Compliant.
- PyLint score of 9.66/10.
- README.md update.

## 17/12/19
- Added Sanity checks for python version and imports.
- __doc__ changes due to error caused by calling __doc__ from textwrap and argparse. __doc__ now requests user call ./bascis.py -h for the original __doc__ message.
- README.me changes.
### Update 2 
- Updated PyTests for new layout of results.
- Added saveoutput function which works with the raw and code outputs.
- Added os and sanity check for directory making.
- Expanded the args required for outter_dorplot function, although this will writen code scores it is the simpler option in this case.
### Update 3
- Formatting changes for Code Styling compliance.
- Script calling examples.
- PyCodeStyle compliant.
- PyLint 9.76/10.
### Update 4
- README.md update.
- README_testing.md updated.
- README_sample_outputs.txt updated.
- README_sample_outputs.txt renamed to .md.
### Update 5
- Added new PyTests to account for --code - test_inner_dotplot_code + code2 + code3.
- Same cannot be applied to outter_dotplot due to requirements from previous function (inner_dotplot).
### Update 6
- Inverted the ASCII and alphabetical options so ASCII is defaulted.
- loadingfiles adapted to be able to accept only 1 file.
- Documentation has been changes to reflect this.
- Changes will cause PyTest Failures.
- Small sentence structure changes.
### Update 7
- PyTest Updated for new outputs.