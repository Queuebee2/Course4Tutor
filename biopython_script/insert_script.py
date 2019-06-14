from DbConnector import DbConnector

DATA_FILE = "new_tab_delimited_stuff.txt"

def main():


    connector = DbConnector()
    print('hh')
    datadict =  {
                'accessiecode': "testcustom",
                'e_value':9e-150,
                'setting_id':1,
                'percentage_identity':11,
                'total_coverage':12,
                'max_scores':13,
                'query_coverage':14
                }
    connector.insert_from_form_data(datadict)

    searchdict = {'resultaat_id':251}
    searchdict2 = {'resultaat_id':251,
                   'resultaat_id':241}
    searchdict3 = {'accessiecode': "testcustom"}
                    
    list_many(connector, [searchdict,
    searchdict2,
    searchdict3])

def list_many(c, dicts):
    for d in dicts:
        listResults(c, d)

    # this is so bad...
def listResults(connector, queryDict):
    results = connector.search_from_form_data(queryDict)

    for i in results:
        print(i)
    """
    with open (DATA_FILE, 'r') as f:

        lines = list(set(f.readlines()))

        for line in lines:
            if isHeaderLine(line):
                pass
            else:
                query, values = genQuery(line.split("\t"), True)
                connector.insert(query, values)
    """
    
    def query_for_formData(formdata):


        values = []
        query_start  = "insert into blast_result("
        query_tables = ""
        
        for k, v in formdata.items():
            query_tables += '`'+str(k)+'`,'
            values.append(v)

        query_tables = query_tables[:-1] # strip ,

        query_end = ")"
        
        query = query_start + query_tables + query_end
        
        return query, values


def isHeaderLine(line):
    """" assume a string/list contains only headers when these keywords exist
    """
    has_title = 'title' in line
    has_score = 'score' in line
    has_matrix = 'matrix' in line

    if has_title and has_score and has_matrix:
        return True
    else:
        return False

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
