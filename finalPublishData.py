import time
import json
import shutil
import csv
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

count = 9
pcstatus = []
sourcefile = ""
# Masukan nama file ke variabel sourcefile

sensor_data = {'Time': "", 'Low': 0, 'High': 0, 'Curr': 0}
THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'BcpiHB2oJQT6VIoPkDBb'
INTERVAL = 5

next_reading = time.time() 
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

client.connect(THINGSBOARD_HOST, 1883, 60)

client.loop_start()

try:
    while True:
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
        
        print(u"Time: %s\Lowest: %d\u00b0C, Highest: %d\u00b0C, Current: %d\u00b0C" % (currTime, lowTemp, highTemp, currTemp))

        sensor_data['Time'] = currTime
        sensor_data['Low'] = lowTemp
        sensor_data['High'] = highTemp
        sensor_data['Curr'] = currTemp

        # Publish ke ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        # Publish ke Mosquitto
        # publish.single("LA03IOT/Time", currTime, hostname="test.mosquitto.org")
        # publish.single("LA03IOT/LowestTemp", lowTemp, hostname="test.mosquitto.org")
        # publish.single("LA03IOT/HighestTemp", highTemp, hostname="test.mosquitto.org")
        # publish.single("LA03IOT/Temp", currTemp, hostname="test.mosquitto.org")

        pcstatus.pop()
        count = count + 1
        print("Done")
        
        next_reading = next_reading + INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()