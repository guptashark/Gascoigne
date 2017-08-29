import webapp2
from homepage import HomePage
from testhandler import TestHandler
from quiz import Quiz
from quiz_result import QuizResult

app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/test', TestHandler),
    ('/quiz', Quiz),
    ('/quiz_result', QuizResult)
], debug=True)
