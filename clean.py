import json
import sqlite3
import urllib


# create SQL database
conn = sqlite3.connect('odd_db.sqlite')
cur = conn.cursor()

# create SQL table
cur.execute('''DROP TABLE IF EXISTS Attributes''')
cur.execute('''CREATE TABLE Attributes(
               EventID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
               Action TEXT,
               ApplicationVersion TEXT,
               Channel TEXT,
               ContentId TEXT,
               ContentThumbnailURL TEXT,
               ContentTitle TEXT,
               ContentType TEXT,
               CreatedAt DATE,
               DeviceBrand TEXT,
               DeviceManufacturer TEXT,
               DeviceModel TEXT,
               DeviceOS TEXT,
               Duration INTEGER,
               Elapsed INTEGER,
               ErrorMessage TEXT,
               Language TEXT,
               Platform TEXT,
               Player TEXT,
               SessionID TEXT,
               UserIP TEXT,
               UserName TEXT,
               VideoSessionID TEXT,
               Viewer TEXT,
               Zip TEXT,
               City TEXT,
               State TEXT,
               Country TEXT)''')

# load json files
with open('odd-events-anon.json') as df:
    for line in df:
        js = json.loads(line)
        
        # since there are missing data, set all variables to None
        contentThumbnailURL, viewer, player, videoSessionID, duration, createdAt, applicationVersion, deviceBrand, deviceManufacturer, platform, userIP,channel, contentType, errorMessage, elapsed, sessionID, contentTitle, userName, deviceOS, deviceModel, language, contentId, action, zip, city, state, country = None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None
        
        # set the variable: key <- value
        for key in js['attributes']:
            print key
            exec(str(key) + " = js['attributes'][key]")
        
        # insert into database
        cur.execute('''INSERT INTO Attributes (Action, ApplicationVersion, Channel, ContentId, ContentThumbnailURL,  ContentTitle, ContentType, CreatedAt, DeviceBrand,  DeviceManufacturer, DeviceModel, DeviceOS, Duration, Elapsed, ErrorMessage, Language, Platform, Player, SessionID, UserIP, UserName, VideoSessionID, Viewer, Zip, City, State, Country) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (action, applicationVersion, channel, contentId, contentThumbnailURL,  contentTitle, contentType, createdAt, deviceBrand,  deviceManufacturer, deviceModel, deviceOS, duration, elapsed, errorMessage, language, platform, player, sessionID, userIP, userName, videoSessionID, viewer, zip, city, state, country))
        conn.commit()



