import webapp2
from base_headers import jinja_env
from google.appengine.api import app_identity
from google.appengine.api import mail

test_integers = [
        ('3 - 5 = ', "ans_01", "-2"),
        ('4 + 7 = ', "ans_02", "11"),
        ('12 - 13 = ', "ans_03", "-1"),
        ('10 - 15 = ', "ans_04", "-5"),
        ('15-10', "ans_05", "5"),
        ('1+1', "ans_06", "2"),
        ('1+2=', "ans_07", "3"),
        ('2+15', "ans_08", "17")]


class Quiz(webapp2.RequestHandler):
    def get(self):
        student_name = self.request.GET['student']
        topic = self.request.GET['topic']
        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render(student = student_name, topic = topic, test = test_integers))

    def post(self):
        num_questions = len(test_integers)
        num_correct = 0
        for question in test_integers:
            student_ans = self.request.POST[question[1]]
            if(student_ans == question[2]):
                num_correct = num_correct + 1
        if(num_correct / float(num_questions) > 0.5):
            self.response.write("You passed the test!")

            mail.send_mail(
                    sender="Aishwary Gupta <guptashark@gmail.com>",
                    to="Aishwary Gupta <guptashark@gmail.com>",
                    subject="Quiz Results",
                    body="You passed the test!")

        else:
            self.response.write("You failed the test. :( ")
            mail.send_mail(
                sender="Aishwary Gupta <guptashark@gmail.com>",
                to="Aishwary Gupta <guptashark@gmail.com>",
                subject="Quiz Results",
                body="You passed the test!")
 
