from controller.base_controller import BaseController


class HelloWorld(BaseController):
    def get(self):
        self._response_json({
            "data": {
                "message": "Hello World!",
            }
        })