import webapp2

class TestHandler(webapp2.RequestHandler):
    def get(self): 
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello World, this is Ash on a testpage!')
