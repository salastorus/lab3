from base_client import BaseClient
import datetime


class ClientGetFriendsAges(BaseClient):
    user_id = None
    method = "friends.get"
    http_method = "GET"

    def __init__(self, user_id):
        self.user_id = user_id

    def get_params(self):
        params = {"user_id": self.user_id, "fields": "bdate"}
        return params

    def response_handler(self, response):
        friends = response["response"]
        ages = []
        for f in friends:
            if "bdate" in f:
                date = f["bdate"] #%d.12.2012
                if len(date)>5:
                    now = datetime.datetime.now()
                    date_time = datetime.datetime.strptime(date, "%d.%m.%Y")
                    age = now - date_time
                    ages.append(age.days//365)
        return ages