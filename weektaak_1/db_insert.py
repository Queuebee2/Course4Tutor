from base64 import b64decode as magic_wizardry
import mysql.connector

HOST_DEFAULT = "hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com"
USER_DEFAULT = "kmoes@hannl-hlo-bioinformatica-mysqlsrv"
DATABASE_DEFAULT = "kmoes"
LOCAL_FIREBALL = False # we need a fireball, conjured by a magician.



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
    


    def insert(self, query):
        """
        example: insert into BLAST_result (Query_id, resultaat_id,
                                           blast_alg_id, acessiecode)
                 values (000000, 000000, 000000, 00000);

        """
        pass
        
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
        if not LOCAL_FIREBALL:
            from sqlmethod import thingy as joke

        lmfao = magic_wizardry(joke)
        fireball = self._DbConnector__wizard_helper(lmfao)

        print("Hocus pocus pilatus pas! Wingardium leviosa! " + \
              "Expecto Patronum!")
        print("Gabindo Purchai Camerinthum Carlem Aber.")

        return fireball




if __name__ == '__main__':
    app = DbConnector()