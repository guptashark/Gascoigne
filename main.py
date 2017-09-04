import webapp2
from homepage import HomePage
from login import Login
from testhandler import TestHandler
from quiz import Quiz
from quiz_result import QuizResult
from quiz_home import QuizHome

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/test', TestHandler),
    ('/quiz', Quiz),
    ('/quiz_home', QuizHome),
    ('/login', Login),
    ('/quiz_result', QuizResult)
], debug=True)
