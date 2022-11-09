from bioseq.calculation.SeqCal import *
from bioseq.pattern.SeqPattern import *
from bioseq.seqMan.dnaconvert import *
# print("in Main.py")

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", default=None, action='store_true',
                             help="Convet DNA to reverse-complementary")

    cgcserch_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    cgcserch_command.add_argument("-r", "--revcomp", default=None, action='store_true',
                             help="Convet DNA to reverse-complementary")
    
    cgcserch_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    cgcserch_command.add_argument("-r", "--revcomp", default=None, action='store_true',
                             help="Convet DNA to reverse-complementary")
    
    cgcserch_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    cgcserch_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")
    cgcserch_command.add_argument("-r", "--revcomp", default=None, action='store_true',
                             help="Convet DNA to reverse-complementary")


    # parser.print_help()
    return parser

def test():
    # Input
    parser = argparserLocal()
    args = parser.parse_args(["cpgScan","-s","AAATTTCCCGGGCGGGGG"])
    print(args)
    print(cpgSearch(args.seq))
    
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    # print(args)
    # print(args.cmd, args.seq)
    # print("Input",args.seq,"\nGC content =", gcContent(args.seq) )

    # if args.seq == None:
    #     print("------\nError: You do not provide -s or --seq\n------\n")
    # else:
    # seq = args.seq.upper()
    # # Input
    # # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        seq = args.seq.upper()
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        seq = args.seq.upper()
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input",args.seq,"\nTranscription =", dna2rna(seq) )  

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        seq = args.seq.upper()
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input",args.seq,"\nTranslation =", dna2protein(seq) )  

    elif args.command == 'enzTargetsScan' :
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        seq = args.seq.upper()
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        print("Input", args.seq, "\n"+args.enz+ " sites =",enzTargetsScan(seq, args.enz))

# print(__name__)
if __name__ == "__main__":
    test()
    # main()