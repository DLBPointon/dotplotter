from basics import outter_dotplot

x = '''
The X axis is: >HeadX = ABCA
The Y axis is: >HeaderY = ACCA

ACCA
====|
A--A|A
----|B
-CC-|C
A--A|A
'''

def test_result_of_outter_dotplot():
	assert outter_dotplot(['A', '-', '-', 'A', '|A\n',
						   '-', '-', '-', '-', '|B\n',
						   '-', 'C', 'C', '-', '|C\n',
						   'A', '-', '-', 'A', '|A\n'],
						   'ABCA', 'ACCA', '>Head', '>Header') == x
