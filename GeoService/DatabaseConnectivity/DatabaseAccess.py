from DatabaseConnectivity import ConnectDatabase

db = ConnectDatabase.Database()

"""Testing Purpose"""

sql = "SELECT * FROM CityDetails "
# # sql Read operation
data = db.sql_read(sql)

print(data)
# # sql Write operation
# print(data)
# sql = "insert into customer_list VALUES(9, 'Sonam', 'Yadav')"

