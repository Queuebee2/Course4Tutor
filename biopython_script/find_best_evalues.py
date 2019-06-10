""" our data is scuffed.
this script takes a dictionary (stored in a pickle file) of result lists
the list contains everything NCBIWWW qblast yields, along with some annotation.

since the dictionary contains multiple lists of just headers (for the csv file),
these are skipped.

prints acession codes along with all found E-values, ordered by E-value.
"""

import pickle
import collections


def main():

    # the pickle file is a scuffed part of the data we saved
    # ironically, it's the healthiest data we have rn.
    
    with open('pickled_data_list.dat', 'rb') as picklefile:

        result_list_of_lists = pickle.load(picklefile)

        print('got',len(set([str(l) for l in result_list_of_lists])),'results')
 
        dicc = dict()
        acessions = []
        
        for result_list in result_list_of_lists:

            
            e_val = result_list[5]
            # test if evalue is actually a digit, since
            # a bunch of items are header lists.
            
            if type(e_val) == float:

                acession =  result_list[1].split("|")[3]

                name = result_list[1].split("|")[4]

                # print found stuff in markdown table format
                # table text can be rendered with atom
                # cells can be copied in to excel
                # cells from excel can be copied into google sheets
                # ( cant copy from atom to sheets )
                print("|",acession,"|",name,"|",e_val,"|")

                acessions.append(acession)

                if acession not in dicc.keys():
                    dicc[acession] = [e_val]
                else:
                    dicc[acession].append(e_val)
                
            else:
                pass
            

        print(len(acessions),'acession codes')
        print(len(set(acessions)),'authentic ones')
        new = []
        for i in acessions:
            if i in new:
                print(i,'already exists')
            new.append(i)
        
        sorted_by_e_val = sorted(dicc.items(), key=lambda kv: kv[1])


        for i in sorted_by_e_val:
            print(i)



def parseGenbank():
    # under here I iterate over some textfile that holds the flat contents
    # of a genbank page
    text_file = open("source_text.txt", 'r')

    lines = []
    for line in text_file:
        lines.append(line.strip())

    findings = []
    countings = dict()
    for item in lines:
        if 'product=' in item:
            product = item.split("=")[1].rstrip("\"").lstrip("\"")
            print(product)
            findings.append(product)
            if product in countings:
                countings[product] +=1
            else:
                countings[product] = 1
            
    # md table the output
    for k,v in countings.items():
        print("|",k,"|",v,"|")


        



