
FILE_1 = "-at-HWI-M02942_file1.txt"
FILE_2 = "-at-HWI-M02942_file2.txt"
FILES = [FILE_1, FILE_2]             # automate finding files later

COMMON_IDENTIFIERS = [
"@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049",
"@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
"@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
"@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760"
]

# we use common identifiers ( identifiers to find fastaQ entry pairs
  # from file 1 and 2 ) for testing purposes/weektaak1
def main():
    print("RUNNING MAIN (FOR TESTING! PROCESSILUMINA V.1")

    # create test files
    data = parseFastaQ(FILES,COMMON_IDENTIFIERS)
    print(data)
            
    print("DONE")

def parseFastaQ(filenames, common_ids,verbose=False):
    """ assume string 'HWI' in every header"""
    
    data = dict()

    for filename in filenames:
        with open (filename, 'r') as f:

            for line in f:
                for identifier in common_ids:
                    if (identifier in line) and (
                            "@HWI" in line):
                        identifier = line
                        data[identifier] = []
                        for i in range(3):
                            data[identifier].append(f.readline().
                                                    replace("\n", ""))


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
            
