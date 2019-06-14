from blastaseq import parseBlast  # args: xml_file-name
from blastaseq import doBlast  # args: query_seq, filename
from processFastQ import parseFastQ  # args: filenames, common_ids

# TO DO
"""
    - refactor code: figure out better names for functions
    - create comprehensible documentation

"""

# IMPORTS
import time
from datetime import datetime
import pickle
import csv
# custom file containing default values and test values
from config.default_constants import *


def main():
    print("running main module's main!")

    # grab {header:[nucseq, qualityscore, qualityASCIImap]}
    # from input file(s)
    # note: first dataset was 2MB 
    header_data_dict = parseFastQ(NEW_BATCH_FILES)

    # show amount of sequences to be blasted
    print(len(header_data_dict))

    # make this into a button later
    input(" press enter start blasting ")

    # APPEND headers to savefile. This can cause
    # multiple rows to contain these headers. deal with it for now or
    # find a better solution ree
    saveData(DEFAULT_HEADERS)

    print("got parsed data from parseFastQ")
    blastcount = 0 # little counter to keep track of progress

    data = dict()  # store values now,
    # in a future script,
    # reroute straight to database without
    # redundant storage within script to
    # reduce memory usage
    
    for header_key, list_value in header_data_dict.items():

        # get sequence string to use for blast query
        # list value format: [sequence(str),qualscore(int),asciimappingqualscore(string)]
        sequence = list_value[0]

        # get seq id, e.g. :2351/1
        # header format = @ghawreiufhiwauefhiawuehfiawehfuw3234324:2342/1
        # changed [-8:-1] to [-8:] to include last character (twin identifier)
        seq_id = header_key[-8:]

        # ------------- carthesian mess incoming -------------
        # here we go through multiple types of blast programs
        # using different databases and different matrices.
        #

        alreadyInSaveFileCount = exists(seq_id, len(BLAST_KWARGS_LIST))
        if alreadyInSaveFileCount:
            print(seq_id, 'already exists', alreadyInSaveFileCount, 'times. skipping')
            pass
        else:
            for kwargs in BLAST_KWARGS_LIST:
                message = 'blasting' + seq_id + " " + str(kwargs)
                # print(message)

                # set sequence in the kwarg dict         
                kwargs['sequence'] = sequence

                # perform a blast through NCBIWWW.qblast
                # an xml file will be created
                doBlast(DEFAULT_BLAST_FILENAME, **kwargs)

                # parse the output xml file
                result_attributes = parseBlast(DEFAULT_BLAST_FILENAME,
                                               verbose=False)

                # ISSUE      # parseBlast just spits out any first result as of now
                # maybe, paramaters could be passed setting boundaries
                # for certain values. e.g. when an e-value is too high,
                # don't parse/write the data
                # ISSUE
                # print(42 * "-")

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

                # count
                blastcount += 1
                do_blast_print = blastcount % 10 == 0
                if do_blast_print:
                    print(blastcount,'sucessful blasts')
                else:
                    pass
                # we REALLY need to make sure blast requests aren't
                # made  too frequently
                # note: in the NCBIWWW module, hardcoded 20-90 second
                # waits are already present.
                # print("doing a quick 13 second nap")
                time.sleep(13)
                
        # toCSV(data)
    print("main done (testprint)")

def exists(identifier, threshold=2, filename=CSV_FILE_NAME):
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
        


def saveData(data, filename=CSV_FILE_NAME):
    # save a line of data to the csv file
    with open(filename, 'a', newline='') as savefile:
        savewriter = csv.writer(savefile, delimiter='\t')
        savewriter.writerow(data)

    with open('pickled_data_list.dat', 'rb') as picklefile:

        try:
            pickleList= pickle.load(picklefile)
            #print('successfully loaded pickle')
        except:
            #print('no pickleDict')
            pickleList = list()

        pickleList.append(data)
        
    with open('pickled_data_list.dat', 'wb') as picklefile:    
        pickle.dump(pickleList, picklefile)


    #print(pickleList)    


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
    # maybe eencorporate the DNA check in the processillumina.parseFastQ
    data = parseFastQ(["-at-HWI-M02942_file1.txt",
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
