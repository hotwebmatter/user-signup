import webapp2

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



<html><head>
    </head>
    <body>
    <h1>Signup</h1>
    
</body></html>
