import RPi.GPIO as GPIO
import time

import sys

sys.path.insert(1, '/home/pi/projects/test_lcm/iust-quadruped/control/')
sys.path.insert(2, '/home/pi/projects/test_lcm/iust-quadruped/control/robot_types/')

import lcm

from robot_types import contact_t


lc = lcm.LCM()
resp = contact_t()

GPIO.setmode(GPIO.BOARD)
contact_pin = 13
GPIO.setup(contact_pin, GPIO.IN)


while(1):
    time.sleep(0.001)
    a=GPIO.input(contact_pin)
    resp.touch = GPIO.input(contact_pin)
    lc.publish("CONTACT", resp.encode())

GPIO.cleanup()