
from processillumina import parseFastaQ

FILE_1 = "-at-HWI-M02942_file1.txt"
FILE_2 = "-at-HWI-M02942_file2.txt"
FILES = [FILE_1, FILE_2]

COMMON_IDENTIFIERS = [
"@HWI-M02942:21:000000000-ACNW4:1:1101:11964:3049",
"@HWI-M02942:21:000000000-ACNW4:1:1101:13265:2250",
"@HWI-M02942:21:000000000-ACNW4:1:1101:23094:3010",
"@HWI-M02942:21:000000000-ACNW4:1:1101:8317:2760"
]

def main():
    print("creating testfiles")

    # get data
    data = parseFastaQ(FILES,COMMON_IDENTIFIERS)

    # reate file1
    output = open("testdata_file1.txt", 'w')
    for r in data:
        if "/1" in r:
            output.write("\n".join([r.replace("\n", "")] + data[r]))
    output.close()

    # create file2
    output = open("testdata_file2.txt", 'w')
    for r in data:
        if "/2" in r:

            output.write("\n".join([r.replace("\n", "")] + data[r]))
                         
    output.close()                  
            
    print("DONE")

if __name__ == "__main__":
    print("running from createTestFiles main()")
    main()
else:
    print("why did you import createTestFiles????")
            
