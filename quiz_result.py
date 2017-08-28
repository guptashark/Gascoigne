import webapp2
from base_headers import jinja_env

class QuizResult(webapp2.RequestHandler):

    """ doesn't make sense for us to get to the "get" version so..."""
    """
    def get(self):
        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render())
    """
    def post(self):


