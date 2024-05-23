class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.ques} : ")
        self.check_answer(ans, current_question.val)

    def check_answer(self, ans, correct_ans):
        if ans.lower() == correct_ans.lower():
            print('Correct!')
        else:
            print('Wrong Answer :(')