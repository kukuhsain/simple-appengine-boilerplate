import webapp2

from controller.home_controller import Home

app = webapp2.WSGIApplication([
    ("/", Home)
], debug=True)
