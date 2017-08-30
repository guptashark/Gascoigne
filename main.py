import webapp2
from homepage import HomePage
from login import Login
from testhandler import TestHandler
from quiz import Quiz
from quiz_result import QuizResult

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/test', TestHandler),
    ('/quiz', Quiz),
    ('/login', Login),
    ('/quiz_result', QuizResult)
], debug=True)
