
import sys
from Adafruit_IO import MQTTClient
from Adafruit_IO import *
from Task1 import task1
from Task1 import a


class task2(task1):
    AIO_FEED_IDs = ["face-mask-check"]
    AIO_USERNAME = "Dungpq1401"
    AIO_KEY = "aio_lkAs23Lfv5m7erwsP3C6rHt9ZFtL"
    def connected(self, client):
        print("Connect successfully ...")
        for feed in self.AIO_FEED_IDs:
            self.client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribe!!!")

    def message(self, client, feed_id, payload):
        print("receive payload: " + payload)
        print("receive feed_id: " + feed_id)

    def execute(self, client):
        self.var = a
        if self.var == 1:
            self.b = "Without face mask"
        elif self.var == 2:
            self.b = "With face mask"
        print("Publishing value: " + str(self.b))
        self.client.publish(self.AIO_FEED_IDs[0], self.b)
    def publish(self):
        self.execute(self.client)

    def __init__(self):
        super().__init__()
        self.client = MQTTClient("Dungpq1401", "aio_lkAs23Lfv5m7erwsP3C6rHt9ZFtL")
        self.client.on_connect = self.connected
        self.client.on_subscribe = self.subscribe
        self.client.on_message = self.message
        self.client.connect()
        self.client.loop_background()

Task2 = task2()

Task2.publish()
Task2.client.loop_background()
