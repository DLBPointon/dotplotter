from basics import inner_dotplot


def test_result_of_inner_dotplot():
	assert inner_dotplot('AB', 'AB') == ['\\', ' ', '|A\n',
													 ' ', '\\', '|B\n']