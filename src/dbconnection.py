import mysql.connector as conn
from config import Settings

class DatabaseConnection:
    def __init__(self):
        self.host = Settings.HOST
        self.username = Settings.USERNAME
        self.password = Settings.PASSWORD
        self.port = Settings.PORT
        self.database = Settings.DATABASE

        # establishing sql connection
        try:
            print("Connecting To Database....!! ")
            self.connection = conn.connect(
                                            host = self.host,
                                            username= self.username,
                                            password = self.password,
                                            database = self.database
                                        )

            print(" Coneection Established Successfully...!!")
            print(self.connection)

        except:
            print("Some Error occured while conecting database...!!")

    def add_easy_questions(self,data):
        pass

    def add_medium_questions(self,data):
        pass

    def add_hard_questions(self,data):
        pass

    def delete_questions(self,difficulty,question_id):
        pass

    def select_table(self,table_name):
        table =  table_name.lower() + Settings.TABLE_POSTFIX
        if table in Settings.TABLE_NAMES:
            pass
        else:
            print("Give a valid table name...!!")


    def close_conection(self):
        try:
            self.connection.close()
            print("Connection to database closed succesfully...!!")

        except:
            print("Some error occured while closing connection....!!")



# if __name__=='__main__':
#     db=DatabaseConnection()
#     db.close_conection()
