import os


class CredentialUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_api_keys():

        client_key = os.environ.get("CLIENT_KEY")
        client_secret = os.environ.get("CLIENT_SECRET")

        if not client_key or not client_secret:
            raise Exception("The API 'CLIENT_KEY' and 'CLIENT_SECRET' must be in the environment variable")
        else:
            return {"CLIENT_KEY": client_key, "CLIENT_SECRET": client_secret}


    def get_db_credentials(self):

        db_user = os.environ.get("DB_USER")
        db_pass = os.environ.get("DB_PASS")

        if not db_user or not db_pass:
            raise Exception("The API 'CLIENT_KEY' and 'CLIENT_SECRET' must be in the environment variable")
        else:
            return {"DB_USER": db_user, "DB_PASS": db_pass}