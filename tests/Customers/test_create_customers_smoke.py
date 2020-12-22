import pytest
import logging as logger
from src.utilities.genericUtility import generate_random_username_email
from src.ApiCalls.CreateCustomers import CreateCustomer
from src.DataAccess.customer_data import CustomerData


@pytest.mark.tcid1
def test_create_custome_only_username_email():

    logger.info("Creating customers")

    rand_info = generate_random_username_email()
    # Email
    email = rand_info['email']

    # Username
    username = rand_info['username']

    # create payload / post file
    cust_obj = CreateCustomer()

    # make the call
    cust_api_info = cust_obj.create_customer(username=username, email=email)

    # verify the user info
    assert cust_api_info['email'] == email, f"Expected email: {email}, but found {cust_api_info['email']}"
    assert cust_api_info['username'] == username, f"Expected username: {username}, but found {cust_api_info['username']}"
    logger.info("username and email are verified from response")

    # verify data in the database
    cust_dao = CustomerData()
    rtn_sql = cust_dao.get_customer_by_email(email)
    logger.info(rtn_sql)

    # Verify email and username with DB
    assert rtn_sql[0]['user_email'] == email, f"Expected Email: {email} but found {rtn_sql[0]['user_email']}"
    assert rtn_sql[0]['user_login'] == username, f"Expected username: {username} but found {rtn_sql[0]['username']}"

