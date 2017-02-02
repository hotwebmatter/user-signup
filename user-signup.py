import webapp2
import cgi
import re

# Regular Expressions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PW_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PW_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

# HTML Template
with open('user-signup.html', 'r') as template_file:
    template = template_file.read()

class MainPage(webapp2.RequestHandler):
    def render_page(self, username='', username_error='', password_error='', verify_error='', email='', email_error=''):
        page = template % {'username': username, 'username_error': username_error, 'password_error': password_error, 'verify_error': verify_error, 'email': email, 'email_error': email_error}
        self.response.out.write(page)

    def get(self):
        self.render_page()

    def post(self):
        errors = False

        username = self.request.get("username")
        username_error = ''
        if not valid_username(username):
            # make a helpful error message
            username_error = cgi.escape("'{0}' is not a valid username.".format(username), quote = True)
            errors = True

        password = self.request.get("password")
        password_error = ''
        verify = self.request.get("verify")
        verify_error = ''
        if not valid_password(password):
            # make a helpful error message
            password_error = cgi.escape("That's not a valid password.", quote = True)
            errors = True

        if password != verify:
            # make a helpful error message
            verify_error = cgi.escape("Your passwords didn't match.", quote = True)
            errors = True

        email = self.request.get("email")
        email_error = ''
        if len(email) > 0 and not valid_email(email):
            # make a helpful error message
            email_error = cgi.escape("That's not a valid email address.", quote = True)
            errors = True

        if errors:
            self.render_page(username, username_error, password_error, verify_error, email, email_error)
            # self.response.write(page)
        else:
            self.redirect("/welcome?username={}".format(username))

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome {0}!".format(username))

routes = [
    ('/', MainPage),
    ('/welcome', WelcomePage)
]

app = webapp2.WSGIApplication(routes, debug=True)
