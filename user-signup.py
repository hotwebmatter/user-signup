import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PW_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PW_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)

def form_element(name, label, required, error):
    result = '''
                <tr>
                    <td><label for="{0}">{1}</label></td>
                    <td>
                        <input name="{0}" '''.format(name, label)
    if name == 'password' or name == 'verify':
        result += 'type="password"'
    else:
        result += 'type="text"'
    result +=' value=""'
    if required:
        result +=' required=""'
    result +='''>
                        '''
    if name == 'username' and 'username' in error:
        result +=''' <span class="error">{0}</span>
                    '''.format(error)
    if name == 'password' and 'That' in error:
        result +=''' <span class="error">{0}</span>
                    '''.format(error)
    if name == 'verify' and 'match' in error:
        result +=''' <span class="error">{0}</span>
                    '''.format(error)
    result += '''</td>
                </tr>
'''
    return result

class MainPage(webapp2.RequestHandler):
    def get(self):
        error_message = self.request.get("error")
        header = """<!DOCTYPE html>
<html>
  <head>
    <title>User Signup</title>
    <style>
        .error {
            color: red;
        }
    </style>
  </head>
  <body>
"""
        footer = """
  </body>
</html>"""

        form_header = """    <h1>User Signup!</h1>
        <form method="post">
            <table>
                <tbody>
"""
        form_body = form_element('username', 'Username', True, error_message)
        form_body += form_element('password', 'Password', True, error_message)
        form_body += form_element('verify', 'Verify Pasword', True, error_message)
        form_body += form_element('email', 'Email', False, error_message)
        form_footer = """            </tbody></table>
            <input type="submit">
        </form>

"""
        form = form_header + form_body + form_footer
        page = header + form + footer
        self.response.write(page)

    def post(self):
        username = self.request.get("username")
        if not valid_username(username):
            # make a helpful error message
            error = "'{0}' is not a valid username.".format(username)
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        password = self.request.get("password")
        verify = self.request.get("verify")
        if not valid_password(password):
            # make a helpful error message
            error = "That's not a valid password."
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        if password != verify:
            # make a helpful error message
            error = "Your passwords didn't match."
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)

        email = self.request.get("email")
        if len(email) > 0 and not valid_email(email):
            # make a helpful error message
            error = "That's not a valid email address."
            error_escaped = cgi.escape(error, quote=True)

            # redirect to homepage, and include error as a query parameter in the URL
            self.redirect("/?error=" + error_escaped)


        self.response.write("Welcome {0}!".format(username))

routes = [
    ('/', MainPage),
]

app = webapp2.WSGIApplication(routes, debug=True)
