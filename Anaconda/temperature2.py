import requests
import sqlite3 as lite
import datetime
import csv

api_key = "8965f08de7f57ed77b96d65225cad0d1"#api key formatted with city, longitude, latitude
url = 'http://api.forecast.io/forecast/'
cities = { "Atlanta": '33.762909,-84.422675', \
"Austin": '30.303936,-97.754355', \
"Boston": '42.331960,-71.020173', \
"Chicago": '41.837551,-87.681844', \
"Cleveland": '41.478462,-81.679435' \
}

end_date = datetime.datetime.now()

con = lite.connect('weather.db')#create the database
cur = con.cursor()
cities.keys()
#print cities.keys()

with con:
   cur.execute('DROP TABLE IF EXISTS daily_temp;')
   with con:  
      cur.execute('CREATE TABLE daily_temp (day_of_reading INT PRIMARY KEY, Atlanta REAL, Austin REAL, Boston REAL, Chicago REAL, Cleveland REAL)')#create the table, specify data types
query_date = end_date - datetime.timedelta(days=30) #set equal to a variable at the start to fix calcuation

with con:
   while query_date < end_date:
      cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (str(query_date.strftime('%Y''%m''%d''%H''%M''%S')),))#date time format works ok
      query_date += datetime.timedelta(days=1)

for k,v in cities.iteritems():#loop and query
   query_date = end_date - datetime.timedelta(days=30) 
   while query_date < end_date:
      qstr=url + api_key + '/' + v + ',' + query_date.strftime('%Y-%m-%dT12:00:00')#call url format and 'don't leave out the '/'
      #print qstr
      #exit()
      r = requests.get(qstr)#query to test script
      #print  r.json()
      #exit()
      
      with con:#
         cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%Y''%m''%d''%H''%M''%S'))
      query_date += datetime.timedelta(days=1) #increment 
      #print  r.json().keys() 
      #exit()
     
con.close()#close connection 
