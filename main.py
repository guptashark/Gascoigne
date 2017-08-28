import webapp2
from homepage import HomePage
from testhandler import TestHandler
from quiz import Quiz

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/test', TestHandler),
    ('/quiz', Quiz)
], debug=True)
