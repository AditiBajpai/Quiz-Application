from user import User


class TakeQuiz:
    def __init__(self,dbc):
        self.dbconnect =dbc

    def display_register_message(self):
        print("Press 1 to start")
        print("Press 2 to Quit")
        print("Enter your Choice")

    def display_message(self):
        print("Press 1 for Easy Level Quiz")
        print("Press 2 for Medium Level Quiz")
        print("Press 3 for Difficult Level Quiz")
        print("Press 4 to Quit")
        print("Enter your Choice")

    def registerUser(self):
        print("Enter your UserName and ID")
        Name = input()
        ID = input()
        u = User(Name, ID)
        print("Registered Successfully....!!")
        return u

    def handleQuizLevel(self,cs,data):
        if cs=="1":
            self.getQuizQuestions("easy",data)
        elif cs=="2":
            self.getQuizQuestions("medium",data)
        elif cs=="3":
            self.getQuizQuestions("hard",data)
        else:
            return

    def displayQuestions(self,data):
        dic = {1:data[2], 2:data[3], 3:data[4], 4:data[5]}
        print(data[1])
        print("Here are your options..!!")
        print("1. "+ data[2])
        print("2. "+ data[3])
        print("3. "+ data[4])
        print("4. "+ data[5])
        print("**********************")
        res = int(input())
        print("**********************")
        print("The correct answer is "+ data[6])
        print("**********************")
        if dic[res].lower() == data[6].lower():
            return True


    def startquiz(self,data):
        total = 0
        print("Here are your questions:")
        print("Select options that is 1,2,3,4")
        for i in data:
            if self.displayQuestions(i):
                total+=1
        return total

    def displayUserDetails(self,record):
        print("ThankYou for participating in the quiz.Here are your details:")
        print("Name = ",record.username)
        print("UserID = ",record.uid)
        print("Score = ", str(record.score))

    def saveResult(self,record):
        self.dbconnect.add_user_details(record)

    def getQuizQuestions(self,dif,record):
        data = self.dbconnect.select_table(dif)
        score = self.startquiz(data)
        record.score = score
        self.displayUserDetails(record)
        self.saveResult(record)


    def run(self):
        choice = None
        while True:
            self.display_register_message()
            choice = input()
            if choice=="1":
                data = self.registerUser()
                self.display_message()
                cs = input()
                self.handleQuizLevel(cs,data)
            else:
                break
