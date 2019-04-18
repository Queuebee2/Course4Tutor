# Author : Milain Lambers
# Github : Queuebee2
# date   : 17-04-2019

version = 12

# notes
# most lines are the standard method for using Bio.Blast.NCBIWWW.qblast
# on a basic level
# TO REFACTOR
# open/seek/close -> with open as

# useful parameters for qblast()
"""  
   - program blastn, blastp, blastx, tblastn, or tblastx (lower case) 
   - database Which database to search against (e.g. "nr"). 
   - sequence The sequence to search. 
   - ncbi_gi TRUE/FALSE whether to give 'gi' identifier. 
   - descriptions Number of descriptions to show. Def 500. 
   - alignments Number of alignments to show. Def 500. 
   - expect An expect value cutoff. Def 10.0. 
   - matrix_name Specify an alt. matrix (PAM30, PAM70, BLOSUM80, BLOSUM45). 
   - filter "none" turns off filtering. Default no filtering 
   - format_type "HTML", "Text", "ASN.1", or "XML". Def. "XML". 
   - entrez_query Entrez query to limit Blast search 
   - hitlist_size Number of hits to return. Default 50 
   - megablast TRUE/FALSE whether to use MEga BLAST algorithm (blastn only) 
   - service plain, psi, phi, rpsblast, megablast (lower case) """

# useful terms
"""
HSP - high scoring segment pair """

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

# hardcodes
TEST_SEQ ='TCCTCGATGAGGTCGTAGATGATCCGGTAGGACTTCATCGGGATGCCGCGGCGCTCGGCGGCCTTGATCACGCTGCCGGGCGGGTTCACGCCGAAGGAGAGCACCGAGGCGCCCGCGGTGCTGGCCAGCAGCAGGTCGGACTCGGTGGGGGCGCCGACCTCGGCCAGCATGATGTCGATCTCGACCTCCTTGGTCGCCTCGGCCTCGCGCAGCAGCCCGCCCTTCGTGGCCCCGAGCGAGCCCTGGGCTCCGGCGCCCCACCCCCGGTTGCTCGTCCTCCTCCTCGGCCTCCGGGACGGGG'
DEFAULT_OUTPUT = "blast_result.xml"

def doBlast(query_seq, filename=DEFAULT_OUTPUT):
    # take a sequence to execute a blastn against the nt database
    # to do : add blasttype, db and matrix parameters

    # open output file
    blast_file = open(filename, 'w')

    # execute blast
    result_handle = NCBIWWW.qblast("blastn", "nt", query_seq)
                                   
    
    # write results ( xml-string )
    blast_file.write(result_handle.read())
    blast_file.seek(0)
    blast_file.close()

def parseBlast(xml_file_name=DEFAULT_OUTPUT):
    # take a filename, asuming it is a textfile with xml formatted blast
    # results and output some standard information

    # NCBIXML.parse method can only be used on a file handle, strings dont work
    blast_file = open(xml_file_name, 'r')
    blast_records = NCBIXML.parse(blast_file)

    
    for blast_record in blast_records:
        for alignment in blast_record.alignments:
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
#ISSUE
# read up on this
# https://biopython.org/DIST/docs/api/Bio.SearchIO._model.hsp-pysrc.html
                # this returns only the values of the
                # first blast result.
                # not sure what to do with the other blasts?
                # maybe implement an e-val (or other) requirement
                # to return stuff by, otherwise, return 'nothing'-values
                # or turn this into a generator and spit out multiple
                # results per header/seq and save both.
                
                # What
                # would be the purpose of keeping multiple results?
                
                blast_file.close()
                return 
    
#/ISSUE
            
def main():
    doBlast(TEST_SEQ)
    parseBlast()
    

if __name__ == "__main__":
    print("running from main blastaseq with default testvalues!")
    main()
else:
    print("succesfully imported blastaseq")
