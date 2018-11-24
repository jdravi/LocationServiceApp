from bs4 import BeautifulSoup
import re


def dms2dd( direction,degrees, minutes, seconds):

    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd


def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]


def parse_dms(latStr, longStr):

    lat = re.split('[^\d\w]+', latStr)
    long = re.split('[^\d\w]+', longStr)

    cal_lat = dms2dd(lat[0],lat[1],lat[2],lat[3])
    cal_long = dms2dd(long[0], long[1], long[2], long[3])
    return cal_lat, cal_long


file_path = "bangData.html"
file = open(file_path)
data = file.read()
soup = BeautifulSoup(data)
table = soup.find("table", attrs={"class":"restable"})

# The first tr contains the field names.
headings = [th.get_text() for th in table.find("tr").find_all("th")]
print(headings)
datasets = []
with open("GeoData.txt","a+") as writeFile:
    for row in table.find_all("tr")[1:]:
        dataset = list(zip(headings, (td.get_text() for td in row.find_all("td"))))
        try:
            city_name = "Hyderabad"
            locality_name = dataset[1][1].split("\xa0")[0]
            lat = dataset[4][1]
            long = dataset[5][1]
            parse_dms(lat, long)

            final_data = city_name + "\t" + locality_name + "\t" + str(parse_dms(lat, long)[0]) + "\t" + str(
                parse_dms(lat, long)[1])+"\n"
            writeFile.write(final_data)
            print(final_data)
        except IndexError as ie:
            print(ie)
        datasets = []
