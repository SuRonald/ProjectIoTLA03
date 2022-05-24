import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print("----------------------------\n")
    client.subscribe("LA03IOT/Time")
    client.subscribe("LA03IOT/LowestTemp")
    client.subscribe("LA03IOT/HighestTemp")
    client.subscribe("LA03IOT/Temp")
 
def on_message(client, userdata, msg):
    if msg.topic == "LA03IOT/Time":
        print("Current Time: " + str(msg.payload, 'UTF-8'))
    
    if msg.topic == "LA03IOT/LowestTemp":
        print("Lowest Temperature: " + str(msg.payload, 'UTF-8') + " Degree Celcius")

    if msg.topic == "LA03IOT/HighestTemp":
        print("Highest Temperature: " + str(msg.payload, 'UTF-8') + " Degree Celcius")

    if msg.topic == "LA03IOT/Temp":
        print("Current Temperature: " + str(msg.payload, 'UTF-8') + " Degree Celcius")
        print("----------------------------\n")
 
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()