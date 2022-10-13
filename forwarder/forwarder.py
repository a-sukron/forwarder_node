#!/usr/bin/env python3
"""PyBluez example read_name.py
Copyright (C) 2014, Oscar Acena <oscaracena@gmail.com>
This software is under the terms of GPLv3 or later.

modified and presented by Ahmad Syukron <ahmad.syukron@live.com>
"""

import sys
import time
import mysql.connector
import paho.mqtt.client as mqtt
from bluetooth.ble import *

class Reader:

    def __init__(self, address):
        self.dt_name=""
        self.dt_val=0
        self.requester = GATTRequester(address, False)
        self.response = GATTResponse()
        self.connect()
        self.request_name()
        self.request_data()
        self.wait_response()
        self.disconnect()
        
    def connect(self):
        sys.stdout.flush()
        self.requester.connect(True)

    def request_data(self):
        self.requester.read_by_handle_async(0x2a, self.response)
    
    def request_name(self):
        data = self.requester.read_by_uuid(
            "00002a00-0000-1000-8000-00805f9b34fb")[0]
        try:
            self.dt_name = data.decode("utf-8")
        except AttributeError:
            self.dt_name = data

    def wait_response(self):
        while not self.response.received():
            time.sleep(0.1)

        data = self.response.received()[0]
        self.dt_val = int.from_bytes(data, "little")
    
    def disconnect(self):
        self.requester.disconnect()
        
    def show(self):
        print(self.dt_name, end =" : ")
        print(self.dt_val)

def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	
if __name__ == "__main__":
    mydb = mysql.connector.connect(
      host="localhost",
      user="sensor_user",
      password="511142011",
      database="sensor"
    )
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io",1883,60)
    saved_val=0
    while 1:
        rx =Reader("8C:AA:B5:86:1F:96")
        if saved_val != rx.dt_val :
            saved_val=rx.dt_val
            i=rx.dt_val
            client.publish('RPI_01/ESP32_001/sensor',payload=i, qos=0, retain=False)
            mycursor = mydb.cursor()
            sql = "UPDATE value SET val=%s WHERE id=%s"
            val = (rx.dt_val, rx.dt_name)
            mycursor.execute(sql, val)
            mydb.commit()
        time.sleep(1)

