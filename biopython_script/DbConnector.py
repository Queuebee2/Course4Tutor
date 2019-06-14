from base64 import b64decode as magic_wizardry
import mysql.connector

HOST_DEFAULT = "hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com"
USER_DEFAULT = "kmoes@hannl-hlo-bioinformatica-mysqlsrv"
DATABASE_DEFAULT = "kmoes"
LOCAL_FIREBALL = True # we need a fireball, conjured by a magician.



class DbConnector():
    """ connection with the database inhere """
    def __init__(self,  host=HOST_DEFAULT, fireball=False,
                        user=USER_DEFAULT, db=DATABASE_DEFAULT):
        
        # intital static attributes
        self.host = host
        self.__magic = fireball
        if not self.__magic:
            self.__magic = self._DbConnector__wizardman()
        self.user = user
        self.db = db

        # variable attributes
        self.connected = False


        # startup
        print("trying to setup a db connection now!")
        
        self._connect()
    

    def select_results(self, limit = 100):
        """ hardcoded select to just select current results"""
        
        self.cursor.execute("SELECT * FROM blast_result LIMIT " + str(limit +";"))

        results = self.cursor.fetchall()

        return results

    def insert_from_form_data(self, formdata):


        values = []
        tables = []
        
        for k, v in formdata.items():
            tables.append(k)
            values.append(v)

        query_tables = ",".join(['`'+str(i)+'`'for i in tables])

        query_end = ")"
        value_placeholders = ','.join(['%s' for item in values])
        query = "insert into blast_result(%s) VALUES(%s);" % (query_tables,
                                                              value_placeholders)

        print(query)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, 'record inserted')
                          

    def search_from_form_data(self, formdata,
                              operator='and',limit=10):


        conditions = ""
        for key, value in formdata.items():
            if type(value) == str:
                conditions += (" ({} LIKE '%{}%') {}".format(key, value, operator))
            else:
                conditions += (" (%s LIKE %s) %s" % (key, value, operator))

        conditions = conditions.rstrip(operator)
                            

        query = ("SELECT * FROM blast_result WHERE %s" % conditions) + " LIMIT "+str(limit)+";"
        print(query)

        
        self.cursor.execute(query)

        results = self.cursor.fetchall()

        return results
            
            
    def insert(self, query, values):
        """
        example: insert into BLAST_result (Query_id, resultaat_id,
                                           blast_alg_id, acessiecode)
                 values (000000, 000000, 000000, 00000);

        """
        
        self.cursor.execute(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, 'record inserted')
        # can't be implemented yet, default values haven't been established
        # it's recommended to set default values on the database side 
        # so the script doesn't haveto generate them for every missing value.

        # extra:
        # add another function to return string query from**kwargs
        # this could be done like ``self.Query_id = blastresult[0]``
        
    def _connect(self):
        # connect to database
        print("trying to connect...")
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                password=self._DbConnector__magic,
                user=self.user,
                db=self.db)

            self.cursor = self.connection.cursor()
            self.connected = True
            print("connection achieved")
        except:
            self.connected = False
            print("No connection established! Did you set the db " + \
                  "connector globals correctly?")
    

    def __wizard_helper(self, bunny):
        # a wizard never reveals it's secret methods
        return bunny.decode("utf-8")
        
    def __wizardman(self):
        # a wizard never reveals it's secret methods
        print("conjuring a fireball...")
        joke = b'QW4zWGFtcGxlU1NBUERST1ckMGwxZDRucjNtM21iM3I0Ymxlbm9ybWFsbHlpanVzdHdyaXRlYWxpdHRsZXN0b3J5bGlrZXRoaXNhbmRpdHNhbHdheXNhZ29vZHBhc3N3b3JkdGhhdHdheQ=='


        lmfao = magic_wizardry(joke)
        fireball = self._DbConnector__wizard_helper(lmfao)

        print("Hocus pocus pilatus pas! Wingardium leviosa! " + \
              "Expecto Patronum!")
        print("Gabindo Purchai Camerinthum Carlem Aber.")

        return fireball




if __name__ == '__main__':
    app = DbConnector()
else:
    print('imported db_insert')
