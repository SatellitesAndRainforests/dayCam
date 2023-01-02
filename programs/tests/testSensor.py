import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 18

while True:
    humidity, temperature = Adafruit_DHT.read_retry( DHT_SENSOR, DHT_PIN )

    if humidity is not None and temperature is not None:
        print( "temp={:.1f}c humidity={:.1f}%".format( temperature, humidity ) )
    else:
        print( "failed to retrieve data from dht sensor")
