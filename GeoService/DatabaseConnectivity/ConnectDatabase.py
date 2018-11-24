import pymysql


class Database(object):

    """DB manager """
    def __init__(self):

        """ Database Connection """
        database_conf = {
            'host': 'localhost',
            'user_name': 'root',
            'database_password': "543213",
            'db_name': "LocationInfo"
        }

        try:
            self._db_connection = pymysql.connect(database_conf['host'], database_conf['user_name'],
                                                  database_conf['database_password'], database_conf['db_name'])

            self._db_cur = self._db_connection.cursor()

        except pymysql.err.InternalError as e:
            print(e)
        except Exception as error:
            print("Error During Database Connection " + str(error))

    def query(self, query, params):

        """This function will perform the sql """
        return self._db_cur.execute(query, params)

    def sql_read(self, sql_statement):

        self._db_cur.execute(sql_statement)
        data = self._db_cur.fetchall()
        return data

    def sql_write(self, sql_statement):
        """Perform write operation on database"""
        data = self._db_cur.execute(sql_statement)
        self._db_connection.commit()
        return data

    def __del__(self):

        try:
            self._db_connection.close()
        except Exception as e:
            print(e)



#
# class Database:
#     classObject = {}
#     newObject = {}
#
#     def __init__(self):
#         # Open database connection
#
#         """ load details from config to connect to any database """
#         self.db = pymysql.connect("localhost", "root", "543213", "LocationInfo")
#         # prepare a cursor object using cursor() method
#         self.cursor = self.db.cursor()
#         Database.classObject['conn'] = self.cursor
#         Database.classObject['db'] = self.db
#
#
#
#     # @staticmethod
#     # def get_db_cursor():
#     #     """returns the connection object  """
#     #     return Database.classObject['conn']
#     #
#     # @staticmethod
#     # def sql_read(db_connect, sql):
#     #     db_connect.execute(sql)
#     #     data = db_connect.fetchall()
#     #     return data
#     #
#     # @staticmethod
#     # def sql_write(db_connect, sql):
#     #
#     #     """This function will perform sql write """
#     #     data = db_connect.execute(sql)
#     #     Database.classObject['db'].commit()
#     #     #Database.classObject['db'].close()
#     #     return data
#
#








