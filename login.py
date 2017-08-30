import webapp2
from base_headers import jinja_env

""" REALLY REALLY BAD!!! no password salting, hashing, nothing!"""
user_dict = {
        'Chloe': 'apple',
        'Zoe': 'orange',
        'Hana': 'pear'}

class Login(webapp2.RequestHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello World, this is Ash!')
        t = jinja_env.get_template('login.html')
        self.response.write(t.render())

    def post(self):
        username = self.request.POST['username']
        correct_password = user_dict[username]
        password = self.request.POST['password']
        if (correct_password == None or correct_password != password):
            # error page!
            t = jinja_env.get_template('failure_login.html')
            self.response.write(t.render())
        else: 
            t = jinja_env.get_template('success_login.html')
            self.response.write(t.render())

        

