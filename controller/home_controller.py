from controller.base_controller import BaseController


class Home(BaseController):
    def get(self):
        self._response_json({
            "data": {
                "message": "Hello World! Welcome to simple-appengine-boilerplate (https://github.com/kukuhsain/simple-appengine-boilerplate.git)",
            }
        })
