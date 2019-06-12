

# imports
from Bio.Blast import NCBIWWW, NCBIXML
from tempfile import SpooledTemporaryFile as virtualFile
from Bio import Entrez
Entrez.email = "MJ.Lambers@student.han.nl" # Always tell NCBI who you are

# hardcodes / defaults
TEST_SEQ ='TTCACGCCGAAGGAGAGCACCGAGGCGCCCGCGGTGCTGGCCAGCAGCAGGTCGGACTCGGTGGGGGCGCCGACCTCGGCCAGCATGATGTCGATCTCGACCTCCTTGGTCGCCTCGGCCTCGCGCAGCAGCCCGCCCTTCGTGGCCCCGAGCGAGCCCTGGGCTCCGGCGCCCCACCCCCGGTTGCTCGTCCTCCTCCTCGGCCTCCGGGACGGGG'
DEFAULT_OUTPUT = "blast_result.xml"
DEFAULT_KWARGS =  {'program': "blastx", 'database': "nr",
                   'expect': 10e-10, 'matrix_name': "BLOSUM62",
                   'hitlist_size':5}


""" qblast and parsing flow """

def blast_without_XML(xml_file_name=DEFAULT_OUTPUT,
                      sequence=False, verbose=False, **kwargs):

    if not kwargs:
        kwargs = DEFAULT_KWARGS
        
    if not sequence:
        sequence = TEST_SEQ
        kwargs['sequence']=sequence
    else:
        pass
        
    
    blast_file = virtualFile(mode='w')

    # from BLASTR with Biopython pdf
    #my_query = SeqIO.read("test.fasta", format="fasta")
    #result_handle = NCBIWWW.qblast("blastn", "nt", my_query.seq)
    
    result_handle = NCBIWWW.qblast(**kwargs)
    blast_file.write(result_handle.read())
    blast_file.seek(0)
    blast_records = NCBIXML.parse(blast_file)
    blast_file.seek(0)

    for r in blast_records:
        print(str(r)[:25])
    blast_records = NCBIXML.parse(blast_file)
    blast_file.seek(0)

    # try reparsing the file after doing .seek(0)
    # spoiler: it works
    blast_records = NCBIXML.parse(blast_file)
    blast_file.seek(0)


    for record in blast_records:
        for alignment in record.alignments:
            for hsp in alignment.hsps:
                print('****Alignment****')
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('score:', hsp.score)
                print('gaps:', hsp.gaps)
                print('e-value:', hsp.expect)
                print(hsp.query[0:90] +'...')
                print(hsp.match[0:90] +'...')
                print(hsp.sbjct[0:90] +'...')




blast_without_XML()
