import webapp2
from base_headers import jinja_env
from google.appengine.api import app_identity
from google.appengine.api import mail

# question, ans_ID, A, B, C, D, correct ans
test_integers = [
        ('3 - 5 = ', "ans_01", "2", "-8", "8", "-2", "-2"),
        ('4 + 7 = ', "ans_02", "-11", "3", "11", "-3", "11"),
        ('2 + 4 = ', "ans_03", "6", "-6", "8", "2", "6"),
        ('8 - 9 = ', "ans_04", "-1", "1", "0", "banana", "-1")]

test_multiplication = [
        ('3 * 5 = ', "ans_01", "10", "9", "3", "15", "15"),
        ('7 * 9 = ', "ans_02", "49", "63", "77", "54", "63"),
        ('7 * 6 = ', "ans_03", "42", "35", "49", "48", "42"),
        ('6 * 5 = ', "ans_04", "32", "16", "elephant", "30", "30")]

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
            "3 < x < 4"),
        ('x(x-1) > 0', "ans_03", 
            "x > -1 and x < 0",
            "0 < x < 1", 
            "x > 1", 
            "x < 0 and x > 1",
            "x < 0 and x > 1"),
        ('(x - 5)(x + 5) < 0', "ans_04",
            "-5 > x > 5",
            "-5 < x < 5",
            "x < -5 and x > 5",
            "no solution",
            "-5 < x < 5"),
        ('(x - 5)(x - 5) > 0', "ans_05", 
            "-5 > x > 5",
            "x > -5",
            "-5 < x < 5",
            "x < 5 or x > 5",
            "x < 5 or x > 5")]

test_quadratic_inequalities_2 = [
        ('x^2 + 5x - 14 < 0', "ans_01",
            "x < -7 and x > 2",
            "x < -2 and x > 7", 
            "-7 < x < 2",
            "-2 < x < 7",
            "-7 < x < 2"),
        ('x^2 - 4x - 45 < 0', "ans_02", 
            "-5 < x < 9",
            "-5 > x > 9",
            "5 < x < -9", 
            "5 > x > -9",
            "-5 < x < 9"),
        ('x^2 + x - 20 > 0', "ans_03",
            "-5 < x < 4",
            "x < -5 or x > 4",
            "x < -5 and x > 4", 
            "4 < x < -5",
            "x < -5 or x > 4"),
        ('x^2 + 15x + 36 > 0', "ans_04",
            "-12 < x < -3",
            "x < -12 and x > -3",
            "x < -12 or x > -3",
            "x < 3 or x > 12",
            "x < -12 or x > -3"),
        ('x^2 - 15x + 36 < 0', "ans_05",
            "3 < x and x < 12",
            "3 < x or x < 12",
            "-12 < x < -3",
            "x < 3 or x > 12",
            "3 < x and x < 12")]


topic_mapping = {
        "integers": test_integers,
        "multiplication": test_multiplication,
        "quadratic inequalities 1": test_quadratic_inequalities_1,
        "quadratic inequalities 2": test_quadratic_inequalities_2}


class Quiz(webapp2.RequestHandler):
    def get(self):
        student_name = self.request.GET['student']
        if student_name == "":
            t = jinja_env.get_template('quiz_home.html')
            self.response.write(t.render(topic_error = "Please enter your name."))
        elif 'topic' not in self.request.GET: 
            t = jinja_env.get_template('quiz_home.html')
            student_name = self.request.GET['student']
            self.response.write(t.render(name_error = "Please select a quiz topic.",
                    student_name = student_name))
        else: 
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


        email_msg = "Student: " + student_name + " did a test on: " + topic + ". "
        email_msg = email_msg + "their score was: " + str(num_correct) + "/" + str(num_questions) + "."
       
        mail.send_mail(
            sender="Aishwary Gupta <guptashark@gmail.com>",
            to="Aishwary Gupta <guptashark@gmail.com>",
            subject="Quiz Results",
            body=email_msg)

"""
            mail.send_mail(
                sender="Aishwary Gupta <guptashark@gmail.com>",
                to="Aishwary Gupta <guptashark@gmail.com>",
                subject="Quiz Results",
                body="You passed the test!")
""" 
