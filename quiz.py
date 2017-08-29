import webapp2
from base_headers import jinja_env

test_integers = [
        ('3 - 5 = ', "ans_01", "-2"),
        ('4 + 7 = ', "ans_02", "11"),
        ('12 - 13 = ', "ans_03", "-1")]


class Quiz(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render(test = test_integers))

    def post(self):
        num_questions = len(test_integers)
        num_correct = 0
        for question in test_integers:
            student_ans = self.request.POST[question[1]]
            if(student_ans == question[2]):
                num_correct = num_correct + 1
        if(num_correct / float(num_questions) > 0.5):
            self.response.write("You passed the test!")
        else:
            self.response.write("You failed the test. :( ")
            
        

