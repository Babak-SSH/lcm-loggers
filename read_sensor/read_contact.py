import RPi.GPIO as GPIO
import time
import sys

import lcm

from data_types import contact_t


# initializing lcm and contact_t data type
lc = lcm.LCM()
resp = contact_t()

GPIO.setmode(GPIO.BOARD)
contact_pin = 13
GPIO.setup(contact_pin, GPIO.IN)
print("Contact ready!")

while(1):
    try:
        # add one millisecond sleep to synchronize it with imu data
        time.sleep(0.001)
        a=GPIO.input(contact_pin)

        resp.touch = GPIO.input(contact_pin)

        lc.publish("CONTACT", resp.encode())
    except KeyboardInterrupt:
        print("Contact closed manually!")
        GPIO.cleanup()
        sys.exit()
