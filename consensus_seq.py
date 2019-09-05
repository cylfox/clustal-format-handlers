
import time
import os
import sys
import getopt
from textwrap import wrap

from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC, SingleLetterAlphabet
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from functions import get_color, get_most_common, read_mafft, most_common_nucleotide
from models import MafftFragment


def main(argv):
    start = time.time()

    input_path = ''
    # path of execution
    output_path = os.path.dirname(os.path.abspath(__file__))
    file = ''
    alignment = []
    # Get all arguments given
    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["inputfile=", "outputfolder=", 'format='])
    except getopt.GetoptError:
        print('consensus_seq.py -i <inputfile> -o <outputfolder> -f <format>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('consensus_seq.py -i <inputfile> -o <outputfolder> -f <format>')
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            if os.path.isabs(arg):
                file = os.path.basename(arg)
                input_path = os.path.dirname(arg)
            else:
                path = os.path.join(os.getcwd(), arg)
                file = os.path.basename(path)
                input_path = os.path.dirname(path)
                # print('path: ' + path + ' file: ' + file + ' inputp: ' + input_path)
        elif opt in ("-o", "--outputfolder"):
            if os.path.isabs(arg):
                output_path = arg
            else:
                output_path = os.path.join(os.getcwd(), arg)
                # print('arg: ' + arg + ' outputp: ' + output_path)
        elif opt in ('-f', '--format'):
            if arg == 'mafft':
                print('Mafft file: ' + file)
                alignment = read_mafft(os.path.join(input_path, file))
            elif arg == 'clustal':
                print('Clustal file: ' + file)
                alignment = AlignIO.read(open(os.path.join(input_path, file)), 'clustal')

    # Declare variables
    repetitions_id = []
    repetitions = 0
    coordinates = 0
    for record in alignment:
        repetitions_id.append(record.id)
        repetitions += 1
        coordinates = len(record)

    # Generate vertical array
    consensus_seq = []
    for i in range(0, coordinates):
        sequence = []
        for j in range(0, repetitions):
            sequence.append(alignment[j][i])
        # print('seq: ' + sequence)
        consensus_seq.append(most_common_nucleotide(''.join(sequence)))
    # ''.join(consensus_seq)
    print(''.join(consensus_seq))
    print(dir(IUPAC))
    #alignment.append(SeqRecord(Seq(consensus_seq, SingleLetterAlphabet()), id='asd', name='putamuerda'))
    print(alignment[0])
    end = time.time()
    print(f'==> Elapsed time: {end - start}')


matplotlib.use('Agg')

if __name__ == "__main__":
    print('consensus_seq v0.1')
    main(sys.argv[1:])

