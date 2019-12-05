seq_1 = 'ABCDDCBA'
seq_2 = 'ABCDDCBA'
lenseq1 = len(seq_2)
lenseq2 = len(seq_1)
inner_plot = []
seqlist1 = []
seqlist2 = []
results_list = []
results = ''
x = 0


def loadingfiles():
    print('not yet')


def inner_dotplot(seq_1, seq_2):
    results_list.append('=' * lenseq1 + '+\n')
    for i in seq_1:
        for j in seq_2:
            if i == j:
                results_list.append(i)
            else:
                results_list.append('-')
        results_list.append('|\n')
    results_list.append('=' * lenseq1 + '+')
    innerplot = ''.join(results_list)
    return innerplot


def outter_dotplot(innerplot, seq_2):
    y = '\\n'
    innerplot = inner_dotplot(seq_1, seq_2)
    for line in innerplot:
        for y in line:
            print('a')

    return 

def plotbuilder(file1, file2):
    print('Builder boii')

def main():
    # seq_1, seq_2, header_1, header_2 = loadingfiles()
    innerplot = inner_dotplot(seq_1, seq_2)
    print(innerplot)
    completeplot = outter_dotplot(innerplot, seq_2)
    return completeplot
   


if __name__ == '__main__':
    main()