
import psycopg2
import random
import math
import datetime

#Latitudes go from -90 to 90
#Longitude go from -180 to 180
numOfDataPoints = 5
numOfNodes = 10
listOfDataPoints = {}
year = 2015
month = 1
day = 1

def dummyDate(year,month,day):
        if(day > 27):
                month += 1
                day = 1
        else:
                day += 1
        temp = '%04d/%02d/%02d' % (year,month,day)
        return str(temp)

try:
        conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='EBmpfDB8NN'")
except:
        print "I am unable to connect to the database"
cur = conn.cursor()


for j in range (0,numOfNodes):
        month = 0
        for i in range (1, numOfDataPoints+1):
                month += 1
                listOfDataPoints[i+numOfDataPoints*j] = {'latitude' : round(random.uniform(-90, 90), 4), 'longitude' : round(random.uniform(-180, 180), 4), 'water_level' : random.randint(1, 6), 'node_number' : j, 'time' : str(datetime.date(year,month,day))}

print listOfDataPoints	

print datetime.date(year,month,day)
print dummyDate(year,month,day)

try:
	
	for pointNum, values in listOfDataPoints.items():

		cur.execute("""INSERT INTO bostonunderwater_node 
		(latitude, longitude, water_level, node_number, time)
		VALUES ({}, {}, {}, {},'2015/02/07')
		""".format(values['latitude'], values['longitude'], values['water_level'], values['node_number']))

		conn.commit()
except:
	print "something failed :("

#'2015/02/07 16:51.01'
