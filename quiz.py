import webapp2
from base_headers import jinja_env
from google.appengine.api import app_identity
from google.appengine.api import mail

# question, ans_ID, A, B, C, D, correct ans
test_integers = [
        ('3 - 5 = ', "ans_01", "2", "-8", "8", "-2", "-2"),
        ('4 + 7 = ', "ans_02", "-11", "3", "11", "-3", "11")]

test_quadratic_inequalities_1 = [
        ('(x-3)(x-4) > 0', "ans_01", 
            "x < 3 or x > 4", 
            "x > 4", 
            "x < -4 and x > -3", 
            "x < 3", 
            "x < 3 or x > 4"),
        ('(x-3)(x-4) < 0', "ans_02", 
            "x < 3 and x > 4", 
            "x > 3", 
            "x < 4", 
            "3 < x < 4", 
            "3 < x < 4")]


topic_mapping = {
        "integers": test_integers,
        "quadratic inequalities 1": test_quadratic_inequalities_1}


class Quiz(webapp2.RequestHandler):
    def get(self):
        student_name = self.request.GET['student']
        topic = self.request.GET['topic']

        # not sure if this is going to work... but we'll try it! 
        topic_test = topic_mapping[topic]

        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render(
            student = student_name, 
            topic = topic, 
            test = topic_test))
        

    def post(self):
        student_name = self.request.POST['student']
        topic = self.request.POST['topic'] 
        topic_test = topic_mapping[topic]
        num_questions = len(topic_test)
        num_correct = 0
        for question in topic_test:
            student_ans = self.request.POST[question[1]]
            if(student_ans == question[6]):
                num_correct = num_correct + 1
       
        passed = False
        result_msg = ""
        if(num_correct / float(num_questions) > 0.5):
            passed = True
            result_msg = "You passed the test!"

        else:
            passed = False
            result_msg = "You failed the test. Maybe you need more practice?" 


        t = jinja_env.get_template('quiz_result.html')
        self.response.write(t.render(
            student = student_name,
            topic = topic,
            num_correct = str(num_correct), 
            num_questions = str(num_questions),
            result_msg = result_msg))
"""
            mail.send_mail(
                    sender="Aishwary Gupta <guptashark@gmail.com>",
                    to="Aishwary Gupta <guptashark@gmail.com>",
                    subject="Quiz Results",
                    body="You passed the test!")
"""
"""
            mail.send_mail(
                sender="Aishwary Gupta <guptashark@gmail.com>",
                to="Aishwary Gupta <guptashark@gmail.com>",
                subject="Quiz Results",
                body="You passed the test!")
""" 
