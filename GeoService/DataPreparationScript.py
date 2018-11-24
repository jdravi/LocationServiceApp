from DatabaseConnectivity import ConnectDatabase
import re


class ReadData(object):

    """This class is all about creating data to Table CityDetails and to LocalityInfo"""

    def __init__(self):
        self.database = ConnectDatabase.Database
        self.db_cursor = ConnectDatabase.Database.get_db_cursor()
        self.file = "final_geo_data.txt"

    def read_data_from_file(self):
        """Reading Geo Data from final_geo_data.txt"""
        lines_seen = set()  # holds lines already seen
        seen_city_name = set()
        return None
        print("Preparing Data...............................")
        with open(self.file,"r") as f:
            header = f.readline()
            for line in f:

                ''' to remove duplicate line '''
                if line not in lines_seen:
                    line_data = line.strip().split("\t")
                    details = {

                        'city_name':line_data[0],
                        'locality_name': re.sub('[^a-zA-Z0-9-_*. ]', '', line_data[1]),
                        'latitude': line_data[2],
                        'longitude': line_data[3]
                    }
                    lines_seen.add(line)

                    '''Query to Enter CityName into CityTable'''
                    city_name = details['city_name'].replace("'", "")
                    if city_name not in seen_city_name:
                        sql_city = """INSERT INTO CityDetails (CityName) VALUES ('%s')"""%(city_name)

                        print(sql_city)
                        res = self.database.sql_write(self.db_cursor,sql_city)
                        seen_city_name.add(city_name)

                    """Select CityId Corresponding to cityName """
                    sql_get_city_id = "SELECT CityId from CityDetails WHERE CityName='%s'" %(city_name)
                    read_result = self.database.sql_read(self.db_cursor,sql_get_city_id)
                    if len(read_result) != 0:
                        city_id = read_result[0][0]

                        """Insert Data into Locality Info """
                        sql_locality = """INSERT INTO  LocalityInfo (LocalityName,CityId,Latitude,Longitude) VALUES ('%s',%s,'%s','%s')"""\
                                       % (details['locality_name'],city_id,details['latitude'],details['longitude'])
                        write_result = self.database.sql_write(self.db_cursor,sql_locality)
                        if write_result:
                            pass
                        else:
                            print("Failed to Insert for Query " + sql_locality)
        print("Data Preparation Complete ...............................")


if __name__ == '__main__':
    rd = ReadData()
    rd.read_data_from_file()

