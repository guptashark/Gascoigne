import webapp2
from base_headers import jinja_env

class QuizHome(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render(test = test_integers))

