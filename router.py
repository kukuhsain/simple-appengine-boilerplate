import webapp2

from controller.hello_controller import HelloWorld

app = webapp2.WSGIApplication([
    ("/", HelloWorld)
], debug=True)
