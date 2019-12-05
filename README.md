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