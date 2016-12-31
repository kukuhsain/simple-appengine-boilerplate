import webapp2

from controller.home_controller import Home
from controller.user_auth_controller import UserRegister, UserLogin, UserLogout

app = webapp2.WSGIApplication([
    ("/", Home),
    ("/api/v1/auth/register", UserRegister),
    ("/api/v1/auth/login", UserLogin),
    ("/api/v1/auth/logout", UserLogout),
], debug=True)
