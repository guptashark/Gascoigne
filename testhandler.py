import webapp2
from base_headers import jinja_env

class TestHandler(webapp2.RequestHandler):
    def get(self): 
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello World, this is Ash on a testpage!')
        t = jinja_env.get_template('test.html')
        self.response.write(t.render())
