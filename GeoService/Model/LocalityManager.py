import json
from collections import defaultdict, OrderedDict

import pymysql
from DatabaseConnectivity import ConnectDatabase
from Model import CityManager


class LocalityManager(object):
    """Managing stuff related to LocalityInfo Table """

    def __init__(self):
        self.database = ConnectDatabase.Database()

    def __call__(self, *args, **kwargs):
        pass

    def get_locality_within_dis(self,user_lat, user_long, dist):

        ''' API, where the user enters a latitude and longitude, and the service
                    returns all the city localities within a geo-distance of 10 kms and sorted on the basis of
                    their respective distance from the user input. '''

        conv = 0.621371
        """calculate miles"""
        miles = dist * conv
        sql = """
        SELECT
        LocalityId,LocalityName,CityId,Latitude,Longitude, (
                3959 * acos(
            cos(radians('%s'))
            * cos(radians(Latitude))
            * cos(radians(Longitude) - radians('%s'))
            + sin(radians('%s'))
            * sin(radians(Latitude))
        )
        )
        AS 
        distance
        FROM
        LocalityInfo
        HAVING
        distance < '%s'
        ORDER
        BY
        distance
        """ % (user_lat, user_long, user_lat,miles)

        """ Perform Sql Query """

        city_id_result = dict()
        try:
            read_result = self.database.sql_read(sql)
            if len(read_result) != 0:
                for eachRow in read_result:
                    template = {}
                    template['LocalityName'] = eachRow[1]
                    template['cityId'] = eachRow[2]
                    template['Distance(in miles)'] = eachRow[5]
                    city_id = template['cityId']
                    if city_id not in city_id_result:
                        city_id_result[city_id] = [template]
                    else:
                        city_id_result[city_id].append(template)

            print(city_id_result)

        except pymysql.err.InternalError as sql_error:
            print(sql_error)

        return city_id_result

    def most_relevent_result_usr(self,user_lat, user_long,limit,user_keyword):

        """:returns list of locality based on user searched keyword """

        sql = """
        SELECT
        LocalityId,LocalityName,CityId,Latitude,Longitude, (
                3959 * acos(
            cos(radians('%s'))
            * cos(radians(Latitude))
            * cos(radians(Longitude) - radians('%s'))
            + sin(radians('%s'))
            * sin(radians(Latitude))
        )
        )
        AS 
        distance
        FROM
        LocalityInfo
        HAVING
        LocalityName LIKE '%s'
        ORDER
        BY
        distance Limit %s
        """ % (user_lat, user_long, user_lat,user_keyword+"%",limit)

        """ Perform Sql Query """
        result = []
        list_of_cityId = {}
        city_mgr = CityManager.CityManager()
        try:
            read_result = self.database.sql_read(sql)
            temp_result = defaultdict(list)
            if len(read_result) != 0:

                for eachRow in read_result:
                    template = dict()
                    template['localityId'] = eachRow[0]
                    template['LocalityName'] = eachRow[1]
                    template['cityId'] = eachRow[2]
                    template['Distance(in miles)'] = eachRow[5]
                    city_id = template['cityId']
                    if city_id not in list_of_cityId:
                        city_res = city_mgr.get_city_datails_based(city_id)
                        if city_res is not None and len(city_res) != 0:
                            template['CityName'] = city_res[0][1]
                            list_of_cityId[city_id] = template['CityName']
                            del template['localityId']
                            temp_result[city_id].append(template)
                    else:
                        template['CityName'] = list_of_cityId[city_id]
                        try:
                            del template['localityId']
                            temp_result[city_id].append(template)

                        except AttributeError:
                            print("attribute problem " + str(city_id))

                result = temp_result
            result = json.dumps(result)
            result = json.loads(result)
        except pymysql.err.InternalError as sql_error:
            print(sql_error)

        finally:
            '''close db connection '''
            pass
        return result


"""Testing API"""
loc_mgr = LocalityManager()
params = {
    'user_text': "xy",
    'lat': 12,
    'lang': 77,
}


