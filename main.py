import webapp2
from jinja2 import Template

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello World, this is Ash!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
