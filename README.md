this codes is created as my solution for firmware engineer's skill test on e-Fishery applying process (Skill Task Firmware Engineer V.1.pdf)

Forwarder node is a Raspberry pi.

Sensor node is an ESP32 ;
sensor node to forwarder node connection : BLE ;
Dummy sensor data : millis()/3000.

MQTT Cloud : broker.emqx.io ; 
MQTT Topic : RPI_01/ESP32_001/sensor/

Database : MySQL ; 
Webserver : HTML with CSS, javascript & PHP

forwarder.py :
- Read advertised BLE data from ESP32 every 1 second;
- Insert data to Mysql database;
- publish data to MQTT cloud

Python Libraries : 
- paho.mqtt;
- mysql.connector;
- pybluez;
- gattlib

Installation :
1. Sensor_node : Upload sensor_node.ino to ESP32 using Arduino IDE;
2. Forwarder Node : Prepare Raspberry pi with Raspbian Buster / Raspbian OS;
  - Install php-mysql & python 3 with its libraries;
  - on mysql, import SQL syntax : sensor.sql
  - create mysql user : sensor_user , password : 511142011
  - copy webserver files to /var/www/html/
  - copy forwarder.py to home diretory and runs it with python 3
