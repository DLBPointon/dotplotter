from basics import outter_dotplot

x = '''
The X axis is: >HeadX = ABCACBA
The Y axis is: >HeaderY = ACCACCA

ACCACCA
=======|
A--A--A|A
-------|B
-CC-CC-|C
A--A--A|A
-CC-CC-|C
-------|B
A--A--A|A
'''

def test_result_of_outter_dotplot():
	assert outter_dotplot(['A', '-', '-', 'A', '-', '-', 'A', '|A\n',
						   '-', '-', '-', '-', '-', '-', '-', '|B\n',
						   '-', 'C', 'C', '-', 'C', 'C', '-', '|C\n',
						   'A', '-', '-', 'A', '-', '-', 'A', '|A\n',
						   '-', 'C', 'C', '-', 'C', 'C', '-', '|C\n',
						   '-', '-', '-', '-', '-', '-', '-', '|B\n',
						   'A', '-', '-', 'A', '-', '-', 'A', '|A\n'],
						   'ABCACBA','ACCACCA', '>Head', '>Header') == x
