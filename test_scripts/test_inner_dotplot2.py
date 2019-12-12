from basics import inner_dotplot


def test_result_of_inner_dotplot2():
	assert inner_dotplot('ABCDEF', 'ABCDEF') == ['A', '-', '-', '-', '-', '-', '|A\n', '-', 'B', '-', '-', '-', '-', '|B\n', '-', '-', 'C', '-', '-', '-', '|C\n', '-', '-', '-', 'D', '-', '-', '|D\n', '-', '-', '-', '-', 'E', '-', '|E\n', '-', '-', '-', '-', '-', 'F', '|F\n']
