
FILE_1 = "-at-HWI-M02942_file1.txt"
FILE_2 = "-at-HWI-M02942_file2.txt"

FILES = [FILE_1, FILE_2]             # automate finding files later


COMMON_IDENTIFIERS = [
"@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049",
"@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
"@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
"@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760"
]

TESTFILE_1 = "testdata_file1.txt"
SCUFFED_XLSX_DATA_SET_FILE = "data_set1.txt"



class ScuffedDataError(BaseException):
    pass



# we use common identifiers ( identifiers to find fastQ entry pairs
  # from file 1 and 2 ) for testing purposes/weektaak1
def main():
    print("RUNNING MAIN (FOR TESTING! PROCESSILUMINA V.1")

    # create test files
    #data = parsefastQ(FILES,COMMON_IDENTIFIERS)
    #print(data)
    parsefastQ([SCUFFED_XLSX_DATA_SET_FILE ,TESTFILE_1], verbose=True)       
        
    print("TESTING DONE")


def parseDoublefastQ(filename, verbose=True):
    """ return a dictionary  in format {Header:[sequence,scoreascii]}
        for a scuffed copy paste of an xlsx workbook tab into notepad"""

    data = dict()

    with open (filename, 'r') as f:

        for line in f:

            [h1, s1, asc1, h2, s2, asc2] = line.split("\t")

            data[h1] = [s1,'noavscore',asc1]
            data[h2] = [s2,'noavscore',asc2[:-2]] # :-2 to remove trailing newline

            if verbose:
                # tested on data_set1, 
                print("H1",h1.split(":")[-1],"allDNA=",all([s in "ATCG" for s in s1]),
                        "H2",h2.split(":")[-1],"allDNA=",all([s in "ATCG" for s in s2]), len(s1), len(s2))
    return data


def checkProperFormat(filename):
    """placeholder function
    - test for a pattern in headers
    - test for conistency in data e.g. lines presented in
    a, b, c, d -> repeat without missing parts
    - test for all([s in "ATCG" for s in seqeunce]
    """
    pass

def testForScuffed(filename):
    """ returns True if a file is tab delimited with both reads on one line
        e.g.
        @Header1\tSeq1\tasciScore1\t@Header2\tSeq2\tasciScore2"""

    with open (filename, 'r') as f:
        line = f.readline()
        if len(line.split("\t")) > 2:
            print("you got scuffed data")
            return True
        else:
            print("That data could be proper fastQ format")
            return False




def parseGoodfastQ(filename, common_ids=[],verbose=False):

    data = dict()
    with open (filename, 'r') as f:
        for line in f:
            for identifier in common_ids:
                has_identifier = identifier in line
                is_header = "@HWI" in line
                if has_identifier and is_header:
                    identifier = line
                    data[identifier] = []
                    for i in range(3):
                        data[identifier].append(f.readline().
                                                replace("\n", ""))
    return data

def parsefastQ(filenames, common_ids=[],verbose=False):
    """ assume string 'HWI' in every header"""

    # filenames should be a list, otherwise, throw error
    if type(filenames) != list:
        raise ValueError("I know it's awkward, but make sure the filename(s) are in a list")
    
    data = dict()

    for filename in filenames:

        # test for scuffed and handle accordingly
        if testForScuffed(filename):
            part_data = parseDoublefastQ(filename)
        else:
            part_data = parseGoodfastQ(filename)
            
        # merge dicts
        data = {**data, **part_data}


    if verbose:
        for k, v in data.items():
            print(k, v)

    print("parsed fasta files!")
    
    return data
    print(10*"-")


    
if __name__ == "__main__":
    print("running from processillumini main!")
    main()
else:
    print("successfully imported processillumina")
            
