import webapp2
from base_headers import jinja_env

basket = ['apple', 'banana', 'orange', 'pear']

class Quiz(webapp2.RequestHandler):
    def get(self):
        t = jinja_env.get_template('quiz.html')
        self.response.write(t.render(basket = basket))
        

