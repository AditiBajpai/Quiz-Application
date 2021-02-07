from dbconnection import DatabaseConnection
from superuser import SuperUser
from config import Settings
from take_quiz import TakeQuiz


class MainQuiz:
    def __init__(self):
        self.dbc = DatabaseConnection()
        self.su = SuperUser(self.dbc)
        self.tq = TakeQuiz(self.dbc)

    def display_message(self):
        print(" Welcome To the Quiz Application....!! ")
        print(" Please Select one of the following options...!!")
        print(" Press 1 to Add/Delete Questions (NOTE: You can add questions only if you are admin/superuser) ....!!")
        print(" Press 2 to Take Part in the Quiz...!!")
        print(" Press 3 to Quit....!!")
        print("Enter Your Choice....!!")


    def run(self):

        choice = None
        while True:
            self.display_message()
            choice = input()

            if choice == "1":
                uname= input("Enter your username...!! ")
                pa= input("Enter your Password...!! ")
                self.su.validate_credentials(uname,pa)

            elif choice == "2":
                self.tq.run()

            else:
                self.dbc.close_conection()
                print("Thank You..!!")
                break




if __name__=='__main__':
    mq = MainQuiz()
    mq.run()
