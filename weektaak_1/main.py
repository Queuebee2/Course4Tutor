from blastaseq import parseBlast        # args: xml_file-name
from blastaseq import doBlast           # args: query_seq, filename
from processillumina import parseFastaQ # args: filenames, common_ids


# TEST VALUES
FILE_1 = "-at-HWI-M02942_file1.txt"
FILE_2 = "-at-HWI-M02942_file2.txt"
FILES = [FILE_1, FILE_2]

COMMON_IDENTIFIERS = [
"@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049",
"@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
"@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
"@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760"
]

DEFAULT_BLAST_FILENAME = "temp_blast.xml"

def main():

    header_data_dict = parseFastaQ(FILES, COMMON_IDENTIFIERS)

    data = dict() # store values now,
                  # in a future script,
                  # reroute straight to database without
                  # redundant storage within script to
                  # reduce memory usage
    for header_key, list_value in header_data_dict.items():
        doBlast(list_value[0], DEFAULT_BLAST_FILENAME) # creates a file
        parseBlast(DEFAULT_BLAST_FILENAME)             # parses file

    # list format [ header, title, length, score, gaps, e-val ]
    
 
main()

