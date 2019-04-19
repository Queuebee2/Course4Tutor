from blastaseq import parseBlast        # args: xml_file-name
from blastaseq import doBlast           # args: query_seq, filename
from processillumina import parseFastaQ # args: filenames, common_ids

import time
#temp import
import csv

# TEST VALUES
FILE_1 = "testdata_file2.txt"
FILE_2 = "testdata_file1.txt"
FILES = [FILE_1, FILE_2]

deprecated = ["@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
              "@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
              "@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760",
              "@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049"]

DEFAULT_BLAST_FILENAME = "temp_blast.xml"

def main():

    header_data_dict = parseFastaQ(FILES, COMMON_IDENTIFIERS)


    ########## TEMPORARY CSV SOLUTION
    with open ("output.csv", 'a') as csvfile:
        print("making temp csv file for test")
        writerhandle = csv.writer(csvfile, delimiter= ',')

        writerhandle.writerow(["header","title","length",
                               "score", "gaps", "e-val" ])
    ########## TEMPORARY CSV SOLUTION

        print("got parsed data from parseFastaQ")
        
        data = dict() # store values now,
                      # in a future script,
                      # reroute straight to database without
                      # redundant storage within script to
                      # reduce memory usage
                      
        for header_key, list_value in header_data_dict.items():
            sequence = list_value[0]
            print("blasting",sequence[:10])
            doBlast(sequence, DEFAULT_BLAST_FILENAME) # creates a file
            
            result_attributes =  parseBlast(DEFAULT_BLAST_FILENAME,
                                            verbose=True)

            print(42*"-")
        # parses file
        # dict format { header: [title, length, score, gaps, e-val ] }
            data[header_key] = result_attributes

        ########## TEMPORARY CSV SOLUTION
            row = [header_key] + result_attributes
            print("writing to csv")
            #row = ",".join([str(i) for i in row])
            writerhandle.writerow(row)
            print(row)
            print(10*"_-")
            
        ########## TEMPORARY CSV SOLUTION
            # we REALLY need to make sure blast requests aren't
            # made  too frequently
            print("doing a quick 10 second nap")
            time.sleep(10)

    
    # toCSV(data)
    print("main done (testprint)")


def toCSV(dataDict):
    # import csv!!!!!
    print("writing dict to csv file")

    with open ("output.csv", 'w') as csvfile:
        writerhandle = csv.writer(csvfile, delimiter= ',')

        writerhandle.writerow(["header","title","length",
                               "score", "gaps", "e-val" ])

        for k , v in dataDict.items():
            row = [k] + v
            writerhandle.writerow(row)

 
main()

