from src.utilities.genericUtility import generate_random_username_email
from src.utilities.requestsUtilities import RequestUtility
import json


class CreateCustomer:

    def __init__(self):
        self.request_utility = RequestUtility()

    def create_customer(self, username=None, email=None, **kwargs):

        if not username and not email:
            ep = generate_random_username_email()
            username = ep['username']
            email = ep['email']

        payload = dict()
        payload['username'] = username
        payload['email'] = email
        payload.update(kwargs)
        payload = json.dumps(payload)

        # make the api call
        created_user_info = self.request_utility.post("customers", payload=payload, expected_status_code=201)
        return created_user_info
