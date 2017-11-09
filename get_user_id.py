from base_client import BaseClient


class GetUserId(BaseClient):
    user_ids = None
    method = 'users.get'

    def __init__(self, user_ids):
        self.user_ids = user_ids

    def get_params(self):
        params = {"user_ids": self.user_ids}
        return params

    def response_handler(self, response):
        return response["response"][0]["uid"]



