import pymysql
from src.utilities.credentialUtility import CredentialUtility
from src.configs.host_config import DB_HOST


class DBUtility(object):

    def __init__(self):
        self.db_helper = CredentialUtility()
        self.db_info = self.db_helper.get_db_credentials()
        self.db_host = DB_HOST["Host"]
        self.db_port = DB_HOST["Port"]

    def create_connection(self):

        connection = pymysql.connect(host=self.db_host, port=self.db_port, user=self.db_info["DB_USER"],
                                     password=self.db_info["DB_PASS"])
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            res_dict = cur.fetchall()
            cur.close()

        except Exception as e:
            raise Exception(f" Failed to execute {sql} \n Error : {str(e)}")
        finally:
            conn.close()

        return res_dict


    def execute_sql(self, sql):
        pass