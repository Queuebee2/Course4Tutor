from blastaseq import parseBlast  # args: xml_file-name
from blastaseq import doBlast  # args: query_seq, filename
from processillumina import parseFastaQ  # args: filenames, common_ids

# TO DO
"""
    - refactor code: figure out better names for functions
    - create comprehensible documentation

"""

# IMPORTS
import time
from datetime import datetime

# temp import (?)
import csv

# TEST VALUES
FILE_1 = "testdata_file2.txt"
FILE_2 = "testdata_file1.txt"
TEST_FILES = [FILE_1, FILE_2]


FIRST_BATCH_FILES = ["-at-HWI-M02942_file1.txt",
         "-at-HWI-M02942_file2.txt"]

NEW_BATCH_FILES = ["data_set1.txt"]

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

# kwargs to use for qblast
BLAST_KWARGS_LIST = [
    {'program': "tblastx", 'database': "nt",
     'expect': 10, 'matrix_name': "BLOSUM62", }
]


#
#
###########################################################################


def main():
    print("running main module's main!")

    # grab {header:[nucseq, qualityscore, qualityASCIImap]}
    # from input file(s)
    # note: first dataset was 2MB 
    header_data_dict = parseFastaQ(NEW_BATCH_FILES)

    # show amount of sequences to be blasted
    print(len(header_data_dict))

    # make this into a button later
    input(" press enter start blasting ")

    # APPEND headers to savefile. This can cause
    # multiple rows to contain these headers. deal with it for now or
    # find a better solution ree
    saveData(DEFAULT_HEADERS)

    # resolved using saveData()
    """   
        ########## TEMPORARY CSV SOLUTION
        with open ("output.csv", 'w') as csvfile:
            print("making temp csv file for test")
            writerhandle = csv.writer(csvfile, delimiter= ',')

            writerhandle.writerow(["header","title","length",
                                   "score", "gaps", "e-val" ])
        ########## TEMPORARY CSV SOLUTION
    """

    print("got parsed data from parseFastaQ")

    data = dict()  # store values now,
    # in a future script,
    # reroute straight to database without
    # redundant storage within script to
    # reduce memory usage

    for header_key, list_value in header_data_dict.items():

        # get sequence string to use for blast query
        sequence = list_value[0]
        # get seq id, e.g. :2351/1
        seq_id = header_key[-8:-1]

        # ------------- carthesian mess incoming -------------
        # here we go through multiple types of blast programs
        # using different databases and different matrices.
        #

        alreadyInSaveFileCount = exists(seq_id, len(BLAST_KWARGS_LIST))
        if alreadyInSaveFileCount:
            print(seq_id, 'already exists', alreadyInSaveFileCount, 'times. skipping')
        else:
            for kwargs in BLAST_KWARGS_LIST:
                message = 'blasting' + seq_id + " " + str(kwargs)
                print(message)

                # set sequence in the kwarg dict         
                kwargs['sequence'] = sequence

                # perform a blast through NCBIWWW.qblast
                # an xml file will be created
                doBlast(DEFAULT_BLAST_FILENAME, **kwargs)

                # parse the output xml file
                result_attributes = parseBlast(DEFAULT_BLAST_FILENAME,
                                               verbose=True)

                # ISSUE      # parseBlast just spits out any first result as of now
                # maybe, paramaters could be passed setting boundaries
                # for certain values. e.g. when an e-value is too high,
                # don't parse/write the data
                # ISSUE
                print(42 * "-")

                # dict format { header: [title, length, score, gaps, e-val ] }
                data[header_key] = result_attributes
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

                result_ids = []
                for k, param in kwargs.items():
                    if k != 'sequence':
                        result_ids.append(param)

                result_ids = result_ids + [timestamp]
                # hack to fix NoneType lists coming from failed/rejected blasts
                # maybe has to do with e-values or actually when nothing comes up
                if not result_attributes:
                    result_attributes = ['nothing' for i in range(5)]
                result_row = [seq_id] + result_attributes + result_ids

                # save found stuff to csvfile (for now)
                # later: this could be a function that
                # inserts the data into a database or
                # uses it to further analyse the origin of the sequence
                # and potential uses
                saveData(result_row)

                # resolved using saveData()
                """
                        ########## TEMPORARY CSV SOLUTION
                            row = [header_key] + result_attributes
                            print("writing to csv")
                            #row = ",".join([str(i) for i in row])
                            writerhandle.writerow(row)
                            print(row)
                            print(10*"_-")
                            
                        ########## TEMPORARY CSV SOLUTION
                """
                # we REALLY need to make sure blast requests aren't
                # made  too frequently
                # note: in the NCBIWWW module, hardcoded 20-90 second
                # waits are already present.
                print("doing a quick 120 second nap")
                time.sleep(120)

        # toCSV(data)
    print("main done (testprint)")

def exists(identifier, threshold=4, filename="savefile.csv"):
    """ identifier: an identifier for a sequence (e.g. a header)
        threshold : the amount of times the identifier can appear
        in the database ( a csv file for now )

        doesn't check whether lines are unique (as of now)
    """
    # this function can later be upgraded to query a database with
    # sql
    
    # checks the results file for  len(BLAST_KWARGS_LIST) amount
    # of header_ids.
    with open(filename, 'r') as savefile:
        count = 0
        for line in savefile:
            if identifier in line:
                count +=1

    if count < threshold:
        return False
    else:
        return count
        


def saveData(data, filename="data_backup.csv"):
    # save a line of data to the csv file
    with open(filename, 'a', newline='') as savefile:
        savewriter = csv.writer(savefile)
        savewriter.writerow(data)


def toCSV(dataDict):
    # import csv!!!!! (move this to a module, maybe?)
    print("writing dict to csv file")

    with open("output.csv", 'w') as csvfile:
        writerhandle = csv.writer(csvfile, delimiter='\t')

        writerhandle.writerow(["header", "title", "length",
                               "score", "gaps", "e-val"])

        for k, v in dataDict.items():
            row = [k] + v
            writerhandle.writerow(row)


def testFastathing():
    # maybe eencorporate the DNA check in the processillumina.parseFastaQ
    data = parseFastaQ(["-at-HWI-M02942_file1.txt",
                        "-at-HWI-M02942_file2.txt"])

    DNAli = [data[x][0] for x in data.keys()]

    # test if every nucleotide sequence under a header
    # is actually DNA
    print(all([(s in "ATCG" for s in dna) for dna in DNAli]))

    for d in data.keys():
        for x in data[d]:
            print(d[:15], x[:15], (all(s in "ATCGN" for s in x)))

        print(31 * "#")


if __name__ == "__main__":
    main()
else:
    print("dont import main as a module pls")
