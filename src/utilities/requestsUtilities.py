import requests
import os
from requests_oauthlib import OAuth1
from src.configs.host_config import API_HOST
from src.utilities.credentialUtility import CredentialUtility
import logging as logger


class RequestUtility(object):

    def __init__(self):

        # get the ENV variable from environment if ENV is not set then default is test
        self.env = os.environ.get("ENV", "test")
        self.baseURL = API_HOST[self.env]
        # As get_api_keys is static method the class does not need to instantiate and no need self
        api_creds = CredentialUtility.get_api_keys()
        self.auth = OAuth1(api_creds["CLIENT_KEY"], api_creds["CLIENT_SECRET"])

    def get(self):
        pass

    def check_stataus_code(self, res_status_code,  expected_status_code):
        assert res_status_code == expected_status_code, \
            f"Expected status code {expected_status_code} but actual {res_status_code}"

    def post(self, endpoint, payload=None, headers=None, expected_status_code=200):

        post_url = self.baseURL + endpoint
        if not headers:
            headers = {
                "Content-Type": "Application/json"
            }

        post_response = requests.post(url=post_url, data=payload, headers=headers, auth=self.auth)
        res_status_code = post_response.status_code

        self.check_stataus_code(res_status_code, expected_status_code)
        rs_jason = post_response.json()
        logger.debug(f"Response Json : \n {rs_jason} \n ########")
        logger.debug(f'Response Status Code {res_status_code} ')
        # assert post_response.status_code == int(expected_status_code), \
        #     f"Expected status code {expected_status_code} but actual {post_response.status_code}"

        return rs_jason
