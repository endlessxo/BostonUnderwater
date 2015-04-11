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
        query = """ SELECT * from bostonunderwater_node WHERE water_level >= '0' """
        print query
        cur.execute(query)

        rows = cur.fetchall()
        dict = {}

        #DATABASE FORMAT
        #ROW 0 = node_number
        #ROW 1 = latitude
        #ROW 2 = longitude
        #ROW 3 = time
        #ROW 4 = water_level

        print "\n Data Pulled From Database: \n"
        for row in rows:
                dict[row[0]] = {'latitude' : str(row[1]), 'longitude' : str(row[2]), 'time' : str(row[3]), 'water_level' : str(row[4]), 'node_number' : str(row[0])}

        print dict

        nodeCount = 0
        plist=[]
        flist=[]

        #For every data entry
        for node in dict:
                #Cast our GPS coords into floats
                lat =  float(dict[node]['latitude'])
                lon = float(dict[node]['longitude'])
                print "\n Point = %d : Lat = %f Long = %f" % (nodeCount,lat,lon)
        
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

        #Append eqfeed_callback funnction 
        output = 'eqfeed_callback(' + dump + ');'
        print output

        outputPath =  os.path.abspath("../bostonunderwater/templates/bostonunderwater/geojson_enc.html")
        with open(outputPath, "w") as text_file:
                text_file.write("%s" % output)

#Encodes the data for each node in a seperate JSON file
def encodeNodeJSON():
        try:
                conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='EBmpfDB8NN'")
        except:
                print "I am unable to connect to the database"

        cur = conn.cursor()
        
        print "Querying Nodes \n"
        for nodeNum in range(0,13):
                #Query data for each node seperately
                query = " SELECT node_number, time, water_level FROM bostonunderwater_node WHERE node_number = '%d" % nodeNum
                query = query + "' "
                print query
                cur.execute(query)
                rows = cur.fetchall()
                dict = {}

                for row in rows:
                        dict[row[0]] = {'time' : str(row[1]), 'water_level' : str(row[2])}
                print dict

                #Print data into string
                node_data = 'data : {"labels":['
                for row in rows:
                        node_data = node_data + str(row[1]) + ','
                node_data = node_data[:-1] + '], "data":['
                for row in rows:
                        node_data = node_data + str(row[2]) + ','
                node_data = node_data[:-1] + ']}'

                print node_data
                
                #Print string to file
                filename = "node" + str(nodeNum) + ".json"
                outputPath = os.path.join("../bostonunderwater/templates/bostonunderwater/nodeData/",filename)
                with open(outputPath, "w") as text_file:
                        text_file.write("%s" % node_data)
                
encodeJSON()
encodeNodeJSON()
