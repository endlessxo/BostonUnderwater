'''
This script connects to the database and runs a simple select from where query in 
postgresql!
It then encodes this information into geoJSON objects and outputs a geoJSON file
'''
import psycopg2
import geojson
import os
from geojson import Point, Feature, FeatureCollection

def encodeJSON():	
        try:
                conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='EBmpfDB8NN'")
        except:
                print "I am unable to connect to the database"

        cur = conn.cursor()
        cur.execute("SELECT * FROM bostonunderwater_node WHERE water_level >= '0'")

        rows = cur.fetchall()
        dict = {}

        #DATABASE FORMAT
        #ROW 0 = node_number
        #ROW 1 = latitude
        #ROW 2 = longitude
        #ROW 3 = time
        #ROW 4 = water_level

        
        for row in rows:
                dict[row[0]] = {'latitude' : str(row[1]), 'longitude' : str(row[2]), 'time' : str(row[3]), 'water_level' : str(row[4]), 'node_number' : str(row[0])}

        print "DATA PULLED FROM DATABASE"
        print dict
        print '\n'

        nodeCount = 0
        plist=[]
        flist=[]
        for node in dict:
                #Cast our GPS coords into floats
                lat =  float(dict[node]['latitude'])
                lon = float(dict[node]['longitude'])
                print "Generating: Point = %d : Lat = %f Long = %f" % (nodeCount,lat,lon)
        
                #Increase nodeCount
                nodeCount += 1

                # Generate point and add to point list
                point = Point((lon,lat))
                plist.append(point)

                # Generate feature w/ properties and add it to feature list
                feature = Feature(geometry=point, properties={"nodeNumber": dict[node]['node_number'], "waterLevel": dict[node]['water_level'], "time": dict[node]['time'], "longitude": dict[node]['longitude'], "latitude": dict[node]['latitude']}, id=str(nodeCount))
                flist.append(feature)

        # Generate Feature Collection and dump to file
        FeatureClct = FeatureCollection(flist)

        #Encode FeatureCollection as JSON
        dump = geojson.dumps(FeatureClct, sort_keys=True)
        output = "eqfeed_callback(" + dump + ");"
        print "\n JSON Output"
        print output
        outputPath = os.path.abspath("../bostonunderwater/templates/bostonunderwater/geojson_enc.html")
        print "\n Print JSON File to Path: " + outputPath + '\n'
        with open(outputPath, "w") as text_file:
                text_file.write("%s" % output)

def encodeNode():
        try:
                conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='EBmpfDB8NN'")
        except:
                print "I am unable to connect to the database"
        cur = conn.cursor()

        for nodeNum in range(0,14):
                query = "SELECT node_number,time,water_level FROM bostonunderwater_node WHERE node_number=" + str(nodeNum)
                #print query
                cur.execute(query)

                rows = cur.fetchall()
                dict = {}

                for row in rows:
                        dict[row[0]] = {'time' : str(row[1]), 'water_level' : str(row[2])}
                print "DB Values for Node %s" % nodeNum
                print dict

                data = 'data : {"labels":['
                for row in rows:
                        data = data + str(row[1]) + ', '
                data = data[:-2] + '], "data": ['
                for row in rows:
                        data = data + str(row[2]) + ', '
                data = data[:-2] + '],}'
                print data

                filename = 'node' + str(nodeNum) + '.json'
                outputPath = os.path.abspath("../bostonunderwater/templates/bostonunderwater/nodeData/%s" % filename)           
                print "Write To Path" + outputPath + "\n"
                with open(outputPath, "w") as text_file:                                                                    
                        text_file.write("%s" % data)

encodeJSON()
encodeNode()
