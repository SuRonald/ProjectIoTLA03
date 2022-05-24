import shutil
import csv
from time import sleep
import paho.mqtt.publish as publish

count = 9
pcstatus = []
sourcefile = ""
# Masukan nama file ke variabel sourcefile

while True:
    sleep(5)
    shutil.copyfile(sourcefile, "tempdata.csv")
    file = open('tempdata.csv','r')
    filecontent = csv.reader(file, delimiter=',')

    for x in range (count):
        next(filecontent)

    pcstatus.append(next(filecontent))

    currTime = pcstatus[0][0]
    lowTemp = int(pcstatus[0][9])
    highTemp = int(pcstatus[0][10])
    currTemp = int(pcstatus[0][1])

    # Publish ke Mosquitto
    publish.single("LA03IOT/Time", currTime, hostname="test.mosquitto.org")
    publish.single("LA03IOT/LowestTemp", lowTemp, hostname="test.mosquitto.org")
    publish.single("LA03IOT/HighestTemp", highTemp, hostname="test.mosquitto.org")
    publish.single("LA03IOT/Temp", currTemp, hostname="test.mosquitto.org")
    
    print(pcstatus[0][0])
    print(pcstatus[0][1])
    print(pcstatus[0][9])
    print(pcstatus[0][10])
    pcstatus.pop()
    count = count + 1
    print("Done")