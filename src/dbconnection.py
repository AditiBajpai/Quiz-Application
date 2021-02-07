import mysql.connector as conn
from config import Settings

class DatabaseConnection:
    def __init__(self):
        self.host = Settings.HOST
        self.username = Settings.USERNAME
        self.password = Settings.PASSWORD
        self.port = Settings.PORT
        self.database = Settings.DATABASE
        self.connection = None
        self.cursor = None

        # establishing sql connection
        try:
            print("Connecting To Database....!! ")
            self.connection = conn.connect(
                                            host = self.host,
                                            username= self.username,
                                            password = self.password,
                                            database = self.database

                                        )
            print(self.connection)
            self.cursor = self.connection.cursor()
            print(" Coneection Established Successfully...!!")


        except:
            print("Some Error occured while conecting database...!!")

    def add_easy_questions(self,data):
        if self.cursor is not None and self.connection is not None:
            sql_query = "INSERT INTO " + Settings.TABLE_EASY + " (question_id, questions, option1, option2, option3 , option4, answer)  VALUES (%s, %s,%s, %s,%s, %s,%s)"
            value = (data.q_id, data.question, data.option1 ,data.option2, data.option3, data.option4, data.answer)
            try:
                self.cursor.execute(sql_query,value)
                self.connection.commit()
                print("Successfully Inserted to easy table quiz..!!")

            except:
                print("Some Error occurd while Insertion...!!")

    def add_medium_questions(self,data):
        if self.cursor is not None and self.connection is not None:
            sql_query = "INSERT INTO " + Settings.TABLE_MEDIUM + " (question_id, questions, option1, option2, option3 , option4, answer)  VALUES (%s, %s,%s, %s,%s, %s,%s)"
            value = (data.q_id, data.question, data.option1 ,data.option2, data.option3, data.option4, data.answer)
            try:
                self.cursor.execute(sql_query,value)
                self.connection.commit()
                print("Successfully Inserted to medium table quiz..!!")

            except:
                print("Some Error occurd while Insertion...!!")

    def add_hard_questions(self,data):
        if self.cursor is not None and self.connection is not None:
            sql_query = "INSERT INTO " + Settings.TABLE_HARD + " (question_id, questions, option1, option2, option3 , option4, answer)  VALUES (%s, %s,%s, %s,%s, %s,%s)"
            value = (data.q_id, data.question, data.option1 ,data.option2, data.option3, data.option4, data.answer)
            try:
                self.cursor.execute(sql_query,value)
                self.connection.commit()
                print("Successfully Inserted to hard table quiz..!!")

            except:
                print("Some Error occurd while Insertion...!!")

    def delete_questions(self,difficulty,question_id):
        table =  difficulty.lower() + Settings.TABLE_POSTFIX
        if table in Settings.TABLE_NAMES:
            id = self.generate_qid(difficulty,question_id)
            if id is not None:
                sql_query = "DELETE FROM " + table + " WHERE question_id = %s"
                tem= (id, )
                self.cursor.execute(sql_query,tem)
                self.connection.commit()
                print("Successfully Deleted from " + difficulty + "  table quiz..!! ")

        else:
            print("Give a valid table name...!!")

    def select_table(self,table_name):
        table =  table_name.lower() + Settings.TABLE_POSTFIX
        if table in Settings.TABLE_NAMES:
            sql_query = "SELECT * FROM " + table + ";"
            self.cursor.execute(sql_query)
            data = self.cursor.fetchall()
            return data
        else:
            print("Give a valid table name...!!")


    def generate_qid(self,diff,qid):
        id = None
        diff = diff.lower()
        if diff == "easy":
            id = Settings.EASY_QID + str(qid)

        elif diff == "medium":
            id = Settings.MEDIUM_QID + str(qid)

        elif diff == "easy":
            id = Settings.HARD_QID + str(qid)

        return id

    def add_user_details(self,udetails):
        if self.cursor is not None and self.connection is not None:
            sql_query = "INSERT INTO " + Settings.TABLE_RESULT + " (user_id, user_name, total_score) VALUES (%s, %s,%s) "
            value = (udetails.uid,udetails.username,udetails.score)
            try:
                self.cursor.execute(sql_query,value)
                self.connection.commit()
                print("Successfully Inserted to Result Table..!!")

            except:
                print("Some Error occurd while Insertion...!!")


    def close_conection(self):
        try:
            self.connection.close()
            print("Connection to database closed succesfully...!!")

        except:
            print("Some error occured while closing connection....!!")



# if __name__=='__main__':
#     db=DatabaseConnection()
#     db.close_conection()
