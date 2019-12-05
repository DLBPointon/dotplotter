seq_1 = 'AB'
seq_2 = 'AB'
lenseq1 = len(seq_2)
lenseq2 = len(seq_1)
inner_plot = []
seqlist1 = []
seqlist2 = []
seq_1backwards = []
results_list = []
results = ''
x = 0


def loadingfiles():
    print('hi')


def inner_dotplot(seq_1, seq_2):
    for i in seq_1:
        for j in seq_2:
            if i == j:
                results_list.append(i)

            else:
                results_list.append('-')
        results_list.append(f'|{i}\n')
    print(results_list)
    return results_list



def outter_dotplot(results_list, seq_2):
    formatting1 = list('=' * lenseq1 + '|\n')
    seqlist1 = list(seq_2)
    results_list = list(seq_2) + formatting1 + results_list
    results_list.insert(lenseq1, '\n')

    #print(results_list)
    allplot = ''.join(results_list)

    return allplot


def plotbuilder(file1, file2):
    print('Builder boii')


def main():
    # seq_1, seq_2, header_1, header_2 = loadingfiles()
    results_list = inner_dotplot(seq_1, seq_2)
    allplot = outter_dotplot(results_list, seq_2)
    print(allplot)


if __name__ == '__main__':
    main()