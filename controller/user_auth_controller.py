from controller.base_controller import BaseController
from model.user import User
from util.token_hashing import TokenHashing


class UserRegister(BaseController):
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")
        name = self.request.get("name")
        phone = self.request.get("phone")

        if email and password:
            user = User.register(email, password, name, phone)
            if user:
                response = {
                    "data": {
                        "access_token": TokenHashing.make_secure_value(str(user.key.id())),
                    }
                }
                self._response_json(response)
            else:
                self._raise_500_response("Email is not available")
        else:
            self._raise_500_response("You must fill all inputs of the form")


class UserLogin(BaseController):
    def post(self):
        username = self.request.get("email")
        password = self.request.get("password")

        user = User.login(username, password)
        if user:
            response = {
                "data": {
                    "access_token": TokenHashing.make_secure_value(str(user.key.id())),
                }
            }
            self._response_json(response)
        else:
            self._raise_401_response("Login failed, wrong email and/or password")


class UserLogout(BaseController):
    def post(self):
        access_token = self.request.get("access_token")
        print access_token
        status = User.logout(access_token)
        if status:
            response = {
                "data": {
                    "message": "Logout Successfully",
                }
            }
            self._response_json(response)
        else:
            self._raise_403_response("Logout Failed")
