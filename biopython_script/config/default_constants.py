
# test.
BOB = 1

# TEST FILES
FILE_1 = "testdata_file2.txt"
FILE_2 = "testdata_file1.txt"
TEST_FILES = [FILE_1, FILE_2]

#@outdated
FIRST_BATCH_FILES = ["-at-HWI-M02942_file1.txt",
                     "-at-HWI-M02942_file2.txt"]

NEW_BATCH_FILES = ["data_set1.txt"]
CSV_FILE_NAME = "data_backup.csv"
# varname says it all
deprecated_ids = ["@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
                  "@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
                  "@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760",
                  "@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049"]

# list of identifiers to check for in the header for each sequence
# in the datafile  (assuming that is fastaq)
# "@HWI" was the standard header of each sequence in the first
# used dataset. change according to your data's headers.
COMMON_IDENTIFIERS = ["@HWI"]

# filename for temporary xml outpust to store blast results
# before being parsed
DEFAULT_BLAST_FILENAME = "temp_blast.xml"

DEFAULT_HEADERS = ["seq id", "title", "length", "score",
                   "gaps", "e-val", 'program', 'database',
                   'expect', 'matrix', 'time']

###########################################################################
#
# PARAMETERS FOR QBLAST
#
# available program parameters for qblast
blast_programs = ['blastn', 'blastp', 'blastx', 'tblastn',
                  'tblastx']

# available databases per program parameter
databases = {'blastn': [],
             'blastp': [],
             'blastx': [],
             'tblastn': [],
             'tblastx': [], }

# available matrices per program parameter
matrices = {'blastn': [],
            'blastp': [],
            'blastx': [],
            'tblastn': [],
            'tblastx': [], }

# kwargs to use for qblast (CURRENT)
BLAST_KWARGS_LIST = [
    {'program': "blastx", 'database': "nt",
     'expect': 10, 'matrix_name': "BLOSUM62", }
]
