import pymysql
from DatabaseConnectivity import ConnectDatabase


class CityManager(object):
    """ Managing method for CityDetail Table """

    def __init__(self):
        pass

    def get_city_detail(self):

        """:return All cityDetails """
        database = ConnectDatabase.Database()
        sql = """SELECT * FROM CityDetails"""
        try:
            read_result = database.sql_read(sql)
        except pymysql.err.InternalError as sql_error:
            print(sql_error)
        return read_result


    def get_city_datails_based(self, city_ids):

        """ :return city details based on given cityIds"""

        database = ConnectDatabase.Database()
        sql = " "
        if type(city_ids) == int:
            sql = "SELECT * FROM CityDetails WHERE CityId = %s " % (city_ids)
        else:

            format_strings = ','.join(['%s'] * len(city_ids))
            print(format_strings)
            sql = 'SELECT * FROM CityDetails WHERE cityId in (' + ','.join((str(n) for n in city_ids)) + ')'

        try:
            read_result = database.sql_read(sql)
            return read_result
        except pymysql.err.InternalError as sql_error:
            print(sql_error)
