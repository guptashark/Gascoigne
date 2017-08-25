import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello World, this is Ash!')
        t = jinja_env.get_template('main.html')
        print self.response.write(t.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
