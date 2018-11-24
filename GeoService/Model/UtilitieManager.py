class UtilityManager(object):

    @staticmethod
    def calculate_distance(user_lat,user_long,model_lat,model_long,dist):

        sql = """
        SELECT
        id, (
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
        markers
        HAVING
        distance < 30
        ORDER
        BY
        distance
        """ %(user_lat,user_long,user_lat)
