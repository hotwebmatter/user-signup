import webapp2
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

class MainPage(webapp2.RequestHandler):
    def get(self):
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

        form = """    <h1>User Signup!</h1>
        <form method="post">
            <table>
                <tbody><tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" required="">
                        <span class="error"></span>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                        <span class="error"></span>
                    </td>
                </tr>
            </tbody></table>
            <input type="submit">
        </form>

"""
        page = header + form + footer
        self.response.write(page)

    def post(self):
        self.response.write("Thanks for trying!")

routes = [
    ('/', MainPage),
]

app = webapp2.WSGIApplication(routes, debug=True)
