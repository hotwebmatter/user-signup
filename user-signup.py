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
    def get(self):
        page = template % {'username': '', "username_error': '', 'password_error': '', 'verify_error': '', 'email': '', 'email_error': ''}
        self.response.write(page)

    def post(self):
        username = self.request.get("username")
        if not valid_username(username):
            # make a helpful error message
            username_error = "'{0}' is not a valid username.".format(username)
            errors = True

        password = self.request.get("password")
        verify = self.request.get("verify")
        if not valid_password(password):
            # make a helpful error message
            password_error = "That's not a valid password."
            errors = True

        if password != verify:
            # make a helpful error message
            verify_error = "Your passwords didn't match."
            errors = True

        email = self.request.get("email")
        if len(email) > 0 and not valid_email(email):
            # make a helpful error message
            email_error = "That's not a valid email address."
            errors = True

        if errors:
            page = template % {'username': username, "username_error': username_error, 'password_error': password_error, 'verify_error': verify_error, 'email': email, 'email_error': email_error}
            self.response.write(page)
        else:
            self.response.write("Welcome {0}!".format(username))

routes = [
    ('/', MainPage),
]

app = webapp2.WSGIApplication(routes, debug=True)
