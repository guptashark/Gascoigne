import webapp2
from homepage import HomePage
from testhandler import TestHandler

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/test', TestHandler)
], debug=True)
