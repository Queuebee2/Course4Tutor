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
    with open('pickled_data_list.dat', 'rb') as picklefile:

        result_list_of_lists = pickle.load(picklefile)

        print('got',len(set([str(l) for l in result_list_of_lists])),'results')



        
        dicc = dict()
        acessions = []
        
        for result_list in result_list_of_lists:

            e_val = result_list[5]
            if type(e_val) == float:

                acession =  result_list[1].split("|")[3]
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

            
main()
