# transcode UserIP into locations with pyipinfodb API

import sqlite3
import urllib
import pyipinfodb
import time

# connect the exist database
conn = sqlite3.connect('odd_db.sqlite')
cur = conn.cursor()

# select existing distince UserIP to trace the locations
# in order to reduce the tracing times
cur.execute('''SELECT DISTINCT UserIP FROM Attributes''')
useriplst = cur.fetchall()

for ip in useriplst:
    
    # check if already updated this IP
    cur.execute('''SELECT DISTINCT Zip FROM Attributes WHERE UserIP = ?;''',  (ip[0],))
    loadedzip = cur.fetchone()
    if loadedzip[0] is not None:
        print 'continue'
        continue
    
    # transcode with API
    apiurl = 'http://api.ipinfodb.com/v3/ip-city/?'
    ip_lookup = pyipinfodb.IPInfo('<ip_key>')
    location = ip_lookup.get_city(ip[0])
    zip = location['zipCode']
    city = location['cityName']
    state = location['regionName']
    country = location['countryName']

    # update database
    cur.execute('''UPDATE Attributes SET Zip = ?, City = ?, State = ?, Country = ? WHERE UserIP = ?;''', (zip, city, state, country, ip[0]))
    conn.commit()

    # slow down the tracing process to meet the API time constrains
    time.sleep(1)
