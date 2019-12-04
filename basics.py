seq_1 = 'ABCABCABC'
seq_2 = 'ABCABCABC'
lenseq1 = len(seq_2)
lenseq2 = len(seq_1)
inner_plot = []
seqlist1 = []
seqlist2 = []
results_list = []
results = ''
x = 0

def inner_dotplot(seq_1, seq_2):
    for i in seq_1:
        for j in seq_2:
            if i == j:
                results_list.append(i)
            else:
                results_list.append('-')
        results_list.append('\n')
    results = ''.join(results_list)
    print(results)

def outter_dotplot():
    print('aye')

inner_dotplot(seq_1, seq_2)