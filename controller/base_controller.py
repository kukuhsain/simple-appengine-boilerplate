import webapp2
import json


class BaseController(webapp2.RequestHandler):
    def _response_json(self, dict_response):
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(dict_response))

    def _response_image(self, image):
        self.response.headers["Content-Type"] = "image/*"
        self.response.out.write(image)

    def _raise_401_response(self, description="Failed Authentication"):
        response = {
            "error": {
                "code": "401",
                "message": description,
            }
        }
        self.response.set_status(401)
        self._response_json(response)

    def _raise_403_response(self, description="Forbidden"):
        response = {
            "error": {
                "code": "403",
                "message": description,
            }
        }
        self.response.set_status(403)
        self._response_json(response)

    def _raise_404_response(self, description="Not Found"):
        response = {
            "error": {
                "code": "404",
                "message": description,
            }
        }
        self.response.set_status(404)
        self._response_json(response)

    def _raise_500_response(self, description="Internal Server Error"):
        response = {
            "error": {
                "code": "500",
                "message": description,
            }
        }
        self.response.set_status(500)
        self._response_json(response)