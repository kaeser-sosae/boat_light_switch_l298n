## Requires Adafruit motorkit
## sudo pip3 install adafruit-circuitpython-motorkit

from adafruit_motorkit import MotorKit
#from adafruit_motorkit import stepper
from adafruit_motor import stepper
from flask import Flask
from flask import request
from flask import render_template
from decimal import Decimal
import time
import board
import pathlib
import sys
import lib8relay
import os

#app = Flask(__name__)
app = Flask(__name__,
            static_url_path='', 
            static_folder='html/includes',
            template_folder='html')

kit_bottom = MotorKit()
kit_top = MotorKit(address=0x61)

# Set the lights when we start up
kit_bottom.motor1.throttle = 0.5
kit_bottom.motor2.throttle = 0.5
kit_bottom.motor3.throttle = 0.5
kit_bottom.motor4.throttle = 0.5
kit_top.motor1.throttle = 0.5
kit_top.motor2.throttle = 0.5
kit_top.motor3.throttle = 0.5
kit_top.motor4.throttle = 0.5

def turn_off(light_number):
        if light_number == "1":
                while kit_bottom.motor1.throttle > 0:
                        kit_bottom.motor1.throttle = kit_bottom.motor1.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "2":
                while kit_bottom.motor2.throttle > 0:
                        kit_bottom.motor2.throttle = kit_bottom.motor2.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "3":
                while kit_bottom.motor3.throttle > 0:
                        kit_bottom.motor3.throttle = kit_bottom.motor3.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "4":
                while kit_bottom.motor4.throttle > 0:
                        kit_bottom.motor4.throttle = kit_bottom.motor4.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "5":
                while kit_top.motor1.throttle > 0:
                        kit_top.motor1.throttle = kit_top.motor1.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "6":
                while kit_top.motor2.throttle > 0:
                        kit_top.motor2.throttle = kit_top.motor2.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "7":
                while kit_top.motor3.throttle > 0:
                        kit_top.motor3.throttle = kit_top.motor3.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        if light_number == "8":
                while kit_top.motor4.throttle > 0:
                        kit_top.motor4.throttle = kit_top.motor4.throttle - float(round(Decimal(0.01), 4))
                        time.sleep(0.01)
        with open('light' + light_number + '.txt', 'w') as f:
                    f.write('0.00')

def set_brightness(light_number, level=0):

        print("Requested to set brightness for light numnber " + light_number + " to " + str(level))

        if light_number == "1":
                if kit_bottom.motor1.throttle < level:
                        while kit_bottom.motor1.throttle < level:
                                kit_bottom.motor1.throttle = kit_bottom.motor1.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_bottom.motor1.throttle > level:
                        while kit_bottom.motor1.throttle > level:
                                kit_bottom.motor1.throttle = kit_bottom.motor1.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "2":
                if kit_bottom.motor2.throttle < level:
                        while kit_bottom.motor2.throttle < level:
                                kit_bottom.motor2.throttle = kit_bottom.motor2.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_bottom.motor2.throttle > level:
                        while kit_bottom.motor2.throttle > level:
                                kit_bottom.motor2.throttle = kit_bottom.motor2.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "3":
                if kit_bottom.motor3.throttle < level:
                        while kit_bottom.motor3.throttle < level:
                                kit_bottom.motor3.throttle = kit_bottom.motor3.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_bottom.motor3.throttle > level:
                        while kit_bottom.motor3.throttle > level:
                                kit_bottom.motor3.throttle = kit_bottom.motor3.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "4":
                if kit_bottom.motor4.throttle < level:
                        while kit_bottom.motor4.throttle < level:
                                kit_bottom.motor4.throttle = kit_bottom.motor4.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_bottom.motor4.throttle > level:
                        while kit_bottom.motor4.throttle > level:
                                kit_bottom.motor4.throttle = kit_bottom.motor4.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "5":
                print("Setting light number 5")
                if kit_top.motor1.throttle < level:
                        while kit_top.motor1.throttle < level:
                                kit_top.motor1.throttle = kit_top.motor1.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_top.motor1.throttle > level:
                        while kit_top.motor1.throttle > level:
                                kit_top.motor1.throttle = kit_top.motor1.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "6":
                if kit_top.motor2.throttle < level:
                        while kit_top.motor2.throttle < level:
                                kit_top.motor2.throttle = kit_top.motor2.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_top.motor2.throttle > level:
                        while kit_top.motor2.throttle > level:
                                kit_top.motor2.throttle = kit_top.motor2.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "7":
                if kit_top.motor3.throttle < level:
                        while kit_top.motor3.throttle < level:
                                kit_top.motor3.throttle = kit_top.motor3.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_top.motor3.throttle > level:
                        while kit_top.motor3.throttle > level:
                                kit_top.motor3.throttle = kit_top.motor3.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
        if light_number == "8":
                if kit_top.motor4.throttle < level:
                        while kit_top.motor4.throttle < level:
                                kit_top.motor4.throttle = kit_top.motor4.throttle + float(round(Decimal(0.01), 4))
                                time.sleep(0.01)
                if kit_top.motor4.throttle > level:
                        while kit_top.motor4.throttle > level:
                                kit_top.motor4.throttle = kit_top.motor4.throttle - float(round(Decimal(0.01), 4))
                                time.sleep(0.01)

        with open('light' + light_number + '.txt', 'w') as f:
            f.write(str(level))

        with open('light' + light_number + '_lastbrightness.txt', 'w') as f:
            f.write(str(level))

def switch_relay(relay_number, value):
        print("Setting relay " + relay_number + " to value " + value)
        lib8relay.set(0,int(relay_number), int(value))
        with open('relay' + relay_number + '.txt', 'w') as f:
            f.write(value)

@app.route('/lights_on', methods=['GET'])
def lights_on():
        light_number = request.args.get('light_number')
        brightness = request.args.get('brightness')
        set_brightness(light_number, float(brightness))
        return "Set light number " + light_number + " to brightness " + brightness

@app.route('/lights_off', methods=['GET'])
def lights_off():
        light_number = request.args.get('light_number')
        turn_off(light_number)
        return "Turned light number " + light_number + " off"

@app.route('/switch_relay_on', methods=['GET'])
def switch_relay_on():
        relay_number = request.args.get('relay_number')
        relay_value = request.args.get('relay_value')
        switch_relay(relay_number, relay_value)
        return "Set relay number " + relay_number + " to value " + relay_value

@app.route('/get_relay_value', methods=['GET'])
def get_relay_value():
        relay_number = request.args.get('relay_number')
        relay_value = lib8relay.get(0,int(relay_number))
        return_val = "off"
        if relay_value == 0:
                return_val = "off"
        if relay_value == 1:
                return_val = "on"
        return return_val

@app.route('/get_light_brightness', methods=['GET'])
def get_light_brightness():
        return_val = ""
        light_number = request.args.get('light_number')
        if light_number == "1":
                return_val = kit_bottom.motor1.throttle
        if light_number == "2":
                return_val = kit_bottom.motor2.throttle
        if light_number == "3":
                return_val = kit_bottom.motor3.throttle
        if light_number == "4":
                return_val = kit_bottom.motor4.throttle
        if light_number == "5":
                return_val = kit_top.motor1.throttle
        if light_number == "6":
                return_val = kit_top.motor2.throttle
        if light_number == "7":
                return_val = kit_top.motor3.throttle
        if light_number == "8":
                return_val = kit_top.motor4.throttle
        return str(round(return_val, 2)) 

@app.route('/get_last_light_brightness', methods=['GET'])
def get_last_light_brightness():
        return_val = ""
        light_number = request.args.get('light_number')

        if os.path.isfile('light' + light_number + '_lastbrightness.txt'):
                with open('light' + light_number + '_lastbrightness.txt', 'r') as reader:
                        return_val = reader.readline().strip()
                        print('Return val:' + return_val)
        return str(round(float(return_val), 2))

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/test", methods=['GET'])
def test():
    return render_template("test.html")    

## Restore the saved states of the lights

if os.path.isfile('relay1.txt'):
        with open('relay1.txt', 'r') as reader:
                switch_relay("1", reader.read())
else:
        switch_relay("1", "0")

if os.path.isfile('relay2.txt'):                
        with open('relay2.txt', 'r') as reader:
                switch_relay("2", reader.read())
else:
        switch_relay("2", "0")

if os.path.isfile('relay3.txt'):
        with open('relay3.txt', 'r') as reader:
                switch_relay("3", reader.read())
else:
        switch_relay("3", "0")

if os.path.isfile('relay4.txt'):
        with open('relay4.txt', 'r') as reader:
                switch_relay("4", reader.read())
else:
        switch_relay("4", "0")

if os.path.isfile('relay5.txt'):
        with open('relay5.txt', 'r') as reader:
                switch_relay("5", reader.read())
else:
        switch_relay("5", "0")

if os.path.isfile('relay6.txt'):
        with open('relay6.txt', 'r') as reader:
                switch_relay("6", reader.read())
else:
        switch_relay("6", "0")

if os.path.isfile('light1.txt'):
        with open('light1.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("1")
                else:
                        set_brightness("1", float(val))
else:
        set_brightness("1", 0.00)

if os.path.isfile('light2.txt'):
        with open('light2.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("2")
                else:
                        set_brightness("2", float(val))
else:
        set_brightness("2", 0.00)

if os.path.isfile('light3.txt'):
        with open('light3.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("3")
                else:
                        set_brightness("3", float(val))
else:
        set_brightness("3", 0.00)

if os.path.isfile('light4.txt'):
        with open('light4.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("4")
                else:
                        set_brightness("4", float(val))
else:
        set_brightness("4", 0.00)

if os.path.isfile('light5.txt'):
        with open('light5.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("5")
                else:
                        set_brightness("5", float(val))
else:
        set_brightness("5", 0.00)

if os.path.isfile('light6.txt'):
        with open('light6.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("6")
                else:
                        set_brightness("6", float(val))
else:
        set_brightness("6", 0.00)

if os.path.isfile('light7.txt'):
        with open('light7.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("7")
                else:
                        set_brightness("7", float(val))
else:
        set_brightness("7", 0.00)

if os.path.isfile('light8.txt'):
        with open('light8.txt', 'r') as reader:
                val = reader.readline().strip()
                if reader.read() == "0.00":
                        turn_off("8")
                else:
                        set_brightness("8", float(val))
else:
        set_brightness("8", 0.00)

## Start the Web Server
app.run(host='0.0.0.0')