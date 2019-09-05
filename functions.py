from models import MafftFragment
from itertools import groupby


def get_color(nucleotide):
    if nucleotide == 'A' or nucleotide == 'a':
        # red
        return [1.0, 0.0, 0.0]
    elif nucleotide == 'C' or nucleotide == 'c':
        # green
        return [0.0, 1.0, 0.0]
    elif nucleotide == 'G' or nucleotide == 'g':
        # blue
        return [0.0, 0.0, 1.0]
    elif nucleotide == 'T' or nucleotide == 't':
        # yellow
        return [1.0, 1.0, 0.0]
    elif nucleotide == 'N' or nucleotide == 'n':
        # white
        return [1.0, 1.0, 1.0]
    else:
        # black
        return [0.0, 0.0, 0.0]


def get_most_common(data, coordinate, repetitions):
    nucleotide_count = [0, 0, 0, 0]
    # print(repetitions)
    repetitions = repetitions - 1
    for rep in range(0, repetitions):
        # print(data[coordinate, rep])
        #print(rep)
        if data[rep, coordinate] == 'A' or data[rep, coordinate] == 'a':
            nucleotide_count[0] += 1
        elif data[rep, coordinate] == 'C' or data[rep, coordinate] == 'c':
            nucleotide_count[1] += 1
        elif data[rep, coordinate] == 'G' or data[rep, coordinate] == 'g':
            nucleotide_count[2] += 1
        elif data[rep, coordinate] == 'T' or data[rep, coordinate] == 't':
            nucleotide_count[3] += 1

    if nucleotide_count[0] > nucleotide_count[1] and nucleotide_count[0] > nucleotide_count[2] and \
            nucleotide_count[0] > nucleotide_count[3]:
        return 'A', nucleotide_count[0]
    elif nucleotide_count[1] > nucleotide_count[0] and nucleotide_count[1] > nucleotide_count[2] and \
            nucleotide_count[1] > nucleotide_count[3]:
        return 'C', nucleotide_count[1]
    elif nucleotide_count[2] > nucleotide_count[1] and nucleotide_count[2] > nucleotide_count[0] and \
            nucleotide_count[2] > nucleotide_count[3]:
        return 'G', nucleotide_count[2]
    elif nucleotide_count[3] > nucleotide_count[1] and nucleotide_count[3] > nucleotide_count[2] and \
            nucleotide_count[3] > nucleotide_count[0]:
        return 'T', nucleotide_count[3]
    else:
        return '-', 0


'''
    Read a file in MAFFT format
    
    :file:  complete path to file
'''
def read_mafft(file):
    with open(file, mode='r') as mafft_file:
        whole = mafft_file.read()
        # print(whole)
        # split headers and rip out the first element (that it's empty)
        whole = whole.split('>')
        whole.pop(0)

        list_whole = []
        for element in whole:
            list_whole.append(element)

        clean_list = []
        for element in list_whole:
            clean_list.append(element.split('\n', 1))

        final_list = []
        for name, seq in clean_list:
            s = seq.replace('\n', '')
            final_list.append(MafftFragment(name, s))
        return final_list


def most_common_nucleotide(sequence):
    #sequence = str(sequence).replace('-', '')
    #print(sequence)
    max_count = 0
    most_common_set = set()

    for char, chars in groupby(sorted(sequence)):
        if not char.isalpha():
            continue

        count = sum(1 for _ in chars)

        if count > max_count:
            most_common_set = {char}
            max_count = count

        elif count == max_count:
            most_common_set.add(char)
    #print(f'common: {most_common_set}')
    try:
        return str(most_common_set.pop())
    except KeyError:
        return '-'
