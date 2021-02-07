from config import Settings
from questions import Questions

class SuperUser:
    def __init__(self,dbc):
        self.dbconnect = dbc

    def validate_credentials(self,uname,password):
        if uname.lower() == Settings.ADMIN_NAME and password == Settings.ADMIN_PASSWORD:
            print("Validation Successfull..!!")
            self.run()
        else:
            print("Invalid Credentials...!!")

    def add_questions(self,ch):
        res = None
        if ch == "1":
            res = self.create_quetion("easy")
            self.dbconnect.add_easy_questions(res)

        elif ch == "2":
            res = self.create_quetion("medium")
            self.dbconnect.add_medium_questions(res)

        elif ch == "3":
            res = self.create_quetion("hard")
            self.dbconnect.add_hard_questions(res)
        else:
            print("Exiting..!!")
            return

    def delete_questions(self,ch):
        if ch == "1":
            id = input("Enter Id of the question you wnat to delete ...!!  ")
            self.dbconnect.delete_questions("easy",id)
        elif ch == "2":
            id = input("Enter Id of the question you wnat to delete ...!!  ")
            self.dbconnect.delete_questions("medium",id)
        elif ch == "3":
            id = input("Enter Id of the question you wnat to delete ...!!  ")
            self.dbconnect.delete_questions("hard",id)

        else:
            return


    def display_message(self):
        print("Press 1 to add Questions..!!")
        print("Press 2 to delete Questions..!!")
        print("Press 3 to Quit..!!")
        print("Enter Your Choice....!!")

    def display_category(self):
        print("Press 1 to add Easy Questions..!!")
        print("Press 2 to add Medium  Questions..!!")
        print("Press 3 to add Hard  Questions..!!")
        print("Press 4 to Quit..!!")
        print("Enter Your Choice....!!")

    def display_delete_category(self):
        print("Press 1 to delete Easy Questions..!!")
        print("Press 2 to delete Medium  Questions..!!")
        print("Press 3 to delete Hard  Questions..!!")
        print("Press 4 to Quit..!!")
        print("Enter Your Choice....!!")

    def create_quetion(self,diff):
        print("Enter question id (any number between 0 to 9)..!!")
        qid = input()
        print("Enter your Question..!!")
        q= input()
        print("Enter option 1..!!")
        o1= input()
        print("Enter option 2..!!")
        o2= input()
        print("Enter option 3..!!")
        o3= input()
        print("Enter option 4..!!")
        o4= input()
        print("Enter correct answer..!!")
        ans = input()

        qs = Questions(diff,q,o1,o2,o3,o4,ans,qid)

        return qs


    def run(self):
        choice = None
        while True:
            self.display_message()
            choice = input()
            if choice == "1":
                self.display_category()
                ch = input()
                self.add_questions(ch)

            elif choice == "2":
                self.display_delete_category()
                ch = input()
                self.delete_questions(ch)

            else:
                break
