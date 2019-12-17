# Output examples
---
## Initial output of the script will include (if everything is stalled and the env is correctly set up):

- Your using at least Version 3.7, You are good to go...
- argparse imported
- numpy imported
- matplotlib imported
- os imported


---
## Output of inner_dotplot function with --code:

- For input strings coming from the file reading function:
	- seq_1:
		- ABCACBA
	- seq_2:
		- ACCACCA

- The output is:
	- resultslist:
		-  ['A', '-', '-', 'A', '-', '-', 'A', '|A\n', 
			'-', '-', '-', '-', '-', '-', '-', '|B\n', 
			'-', 'C', 'C', '-', 'C', 'C', '-', '|C\n',
			'A', '-', '-', 'A', '-', '-', 'A', '|A\n',
			'-', 'C', 'C', '-', 'C', 'C', '-', '|C\n',
			'-', '-', '-', '-', '-', '-', '-', '|B\n',
			'A', '-', '-', 'A', '-', '-', 'A', '|A\n']
		- Although somewhat disorganised it has allowed great flexability.
---

## Out put of outter_dotplot function

- For the input of:
	- resultslist
	- seq_1
	- seq_2

- The output is:
	- theplot:
		-	The X axis is: >Head
			X = ABCACBA
			The Y axis is: >Header
			Y = ACCACCA

			ACCACCA
			=======|
			A--A--A|A
			-------|B
			-CC-CC-|C
			A--A--A|A
			-CC-CC-|C
			-------|B
			A--A--A|A
---

## Output:
For the same input sequences.

- For inner_dotplot:
	- resultslist:
		- ['\\', ' ', ' ', '\\', ' ', ' ', '\\', '|A\n',
		      ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|B\n',
		  ' ', '\\', '\\', ' ', '\\', '\\', ' ', '|C\n',
		   '\\', ' ', ' ', '\\', ' ', ' ', '\\', '|A\n',
		  ' ', '\\', '\\', ' ', '\\', '\\', ' ', '|C\n',
		      ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|B\n',
		   '\\', ' ', ' ', '\\', ' ', ' ', '\\', '|A\n']
		- The visual formatting inconsistancy is caused by the size of \\ compared to ' '.

- For outter_dotplot:
	- theplot:
		- 	The X axis is: >Head
			X = ABCACBA
			The Y axis is: >Header
			Y = ACCACCA

			ACCACCA
			=======|
			\  \  \|A
			       |B
			 \\ \\ |C
			\  \  \|A
			 \\ \\ |C
			       |B
			\  \  \|A

---

## Matplotfunction output
For the sequence above the --matplot flag will not produce anything on the commandline but will create a new window with the correct matplot graph.

- ![alt text](https://github.com/ARU-Bioinf-IBDS/coursework-DLBPointon/blob/master/matplot_example.png 'Example of the --matplot flag')
---
