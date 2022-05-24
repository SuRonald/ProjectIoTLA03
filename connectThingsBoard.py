import time
import paho.mqtt.client as mqtt
import json

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
        currTime = "15:10:10"
        HD0 = 35.7
        HD1 = 41.0
        
        currTime = "15:10:10"
        lowTemp = 43
        highTemp = 75
        currTemp = 65
        
        print(u"Time: %s\Lowest: %d\u00b0C, Highest: %d\u00b0C, Current: %d\u00b0C" % (currTime, lowTemp, highTemp, currTemp))

        sensor_data['Time'] = currTime
        sensor_data['Low'] = lowTemp
        sensor_data['High'] = highTemp
        sensor_data['Curr'] = currTemp

        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading = next_reading + INTERVAL
        sleep_time = next_reading - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()