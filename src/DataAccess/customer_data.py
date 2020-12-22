from src.utilities.dbUtility import DBUtility


class CustomerData(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):
        sql = f"SELECT * FROM local.wp_users WHERE user_email='{email}';"
        res_sql = self.db_helper .execute_select(sql)
        return res_sql
