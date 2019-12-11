#Example file for parsing and processing JSON

import urllib.request
import json
import ssl

def printResults(data):
    theJSON=json.loads(data)
    #accessing the content of the JSON like an object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count=theJSON["metadata"]["count"]
    print(str(count)+" events recorded")

    #printing additional data like place where it occured
    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("-----------------------------------\n")

    #events have magnitude more than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"]>=4.0:
            print("%2.1f" %i["properties"]["mag"], i["properties"]["place"])
    print("-----------------------------------\n")

    #events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in theJSON["features"]:
        feltReports=i["properties"]["felt"]
        if feltReports!=None:
            if feltReports>0:
                print("%2.1f" %i["properties"]["mag"], i["properties"]["place"], " reported "+str(feltReports)+" times")

#print json data from http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson where at least 1 person reported feeling something
def main():
   
    #urlData="https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"
    urlData="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    context = ssl._create_unverified_context()
    webUrl=urllib.request.urlopen(urlData, context=context)

    #webUrl=urllib.request.urlopen(urlData)
    print("result code: "+str(webUrl.getcode()))
    if(webUrl.getcode()==200):
        data=webUrl.read()
        printResults(data)
    else:
        print("Received error, can't parse the results")


if __name__ == "__main__":
    main()