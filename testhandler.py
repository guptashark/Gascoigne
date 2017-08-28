import webapp2
from base_headers import jinja_env

class TestHandler(webapp2.RequestHandler):
    def get(self): 
        """ Writing without specifying content type... """ 
        """ 
        self.response.write('Hello World')
        """ 
       
        """ Writing with content type specification as html """ 
        """ 
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello World, this is Ash on a testpage!')
        """ 

        """ Writing by using the templating engine to render a template """ 
        
        t = jinja_env.get_template('test.html')
        self.response.write(t.render())

    def post(self):
        t = jinja_env.get_template('test_post.html')
        self.response.write(t.render())
        
        
