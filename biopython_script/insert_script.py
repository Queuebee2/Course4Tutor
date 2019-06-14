from db_insert import DbConnector
from DbConnector import DbConnector

DATA_FILE = "new_tab_delimited_stuff.txt"

def main():


    connector = DbConnector()
    with open (DATA_FILE, 'r') as f:

        lines = list(set(f.readlines()))

        for line in lines:
            if 'title' in line and 'score' in line and 'matrix' in line:
                pass
            else:

                query, values = genQuery(line.split("\t"), True)
                connector.insert(query, values)



"""Queries (for now) are specific to
insert into settings(id, `database`, alg_naam, scorematrix)
Values(1,'nt','tblastx','BLOSUM62');


so, id 1 on the settings_id"""

def genQuery(l,verbose=False):

    
    seq_id = l[0] #UNUSED
    print(l)
    try:
        accessiecode = l[1].split("|")[3] # not certain
    except:
        accessiecode = None # will result in "NULL"
        # some erro
    e_value = str(l[6])
    percentage_identity = '' #UNUSED
    total_coverage = '' #UNUSED
    query_coverage = '' #UNUSED
    max_scores = '' #UNUSED
    sequentie = '' # not kept track of in right way
    setting_id = 1
    eiwit_id = '' #UNUSED
    Geslachtsnaam_id = '' #UNUSED
    
    query = """insert into blast_result(
                                     `accessiecode`, `e_value`, `setting_id`)
                            Values  (%s,%s,%s);"""

    # erm. so, if acession id = None, e_val turns into tblastx. Nice.
    # fix please
    if e_value == 'tblastx':
        e_value = None
        
    values = (accessiecode,e_value , int(setting_id),)

    if verbose:
        print(l)
        print(accessiecode, e_value, setting_id)
        print(query, values)
    return query, values


if __name__ == '__main__':
    main()
else:
    print('imported insert_script')
