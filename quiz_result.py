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
       # self.response.write("Yay!") 
        name = self.request.POST['ans_1']
        if(name == "7"):
            self.response.write("you got the first question right!")
        else:
            self.response.write("you got the first question wrong!")
        
         


