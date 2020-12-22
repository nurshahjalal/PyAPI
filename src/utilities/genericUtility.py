import random
import logging as logger
import string


def generate_random_username_email(domain=None, prefix=None):
    logger.debug("Generating Random Username and Email")

    if not domain :
        domain = "randomtest.com"
    if not prefix:
        prefix = "testuser"

    random_string = "".join(random.choices(string.ascii_lowercase, k= 10 ))
    username = prefix + "." + random_string
    email = prefix + "_" + random_string + "@" + domain

    random_info = {'username': username, 'email': email}
    logger.debug(f'Randomly generated username and email is {random_info}')

    return random_info
