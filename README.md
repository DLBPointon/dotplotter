# Coursework-1836811

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
- Recap on PyTests.
	- InnerDotplot tests all pass.
	- OutterDotplot tests all pass.

## 13/12/19
- Started of a propper filter implimentation which will replace singluar matches with '.' rather than '\\'.
- This function works but struggles when it comes to the end of the list - index out of range error.
- Changes to command structure for flexibility of flag usage.