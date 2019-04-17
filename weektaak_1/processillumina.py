
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
    """memes"""

    data = dict()

    for filename in FILES:
        with open (filename, 'r') as f:

            for line in f:
                for identifier in COMMON_IDENTIFIERS:
                    if identifier in line:
                        identifier = line
                        data[identifier] = []
                        for i in range(3):
                            data[identifier].append(f.readline().
                                                    replace("\n", ""))



        for k, v in data.items():
            print(k, v)

    print(10*"-")
    
    print(10*"-")

main()
            
