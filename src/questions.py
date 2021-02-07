from config import Settings

class Questions:
    def __init__(self,diff,question,op1,op2,op3,op4,ans,id):
        self.option1=op1
        self.option2=op2
        self.option3=op3
        self.option4=op4
        self.answer = ans
        self.question = question
        self.q_id = self.create_question_id(self,diff,id)

    def create_question_id(self,diff,id):
        q_id = None
        if diff.lower() == 'easy':
            qid = Settings.EASY_QID+str(id)

        elif diff.lower() == 'hard':
            qid = Settings.HARD_QID+str(id)

        elif diff.lower() == 'medium':
            qid = Settings.MEDIUM_QID+str(id)

        return q_id
