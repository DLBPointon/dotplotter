from basics import inner_dotplot


def test_result_of_inner_dotplot2():
	assert inner_dotplot('ABCDEF', 'ABCDEF') == ['\\', ' ', ' ', ' ', ' ', ' ', '|A\n',
															' ', '\\', ' ', ' ', ' ', ' ', '|B\n',
															' ', ' ', '\\', ' ', ' ', ' ', '|C\n',
															' ', ' ', ' ', '\\', ' ', ' ', '|D\n',
															' ', ' ', ' ', ' ', '\\', ' ', '|E\n',
															' ', ' ', ' ', ' ', ' ', '\\', '|F\n']
