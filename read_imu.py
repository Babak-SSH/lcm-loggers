import serial
import time
import numpy as np
import sys

sys.path.insert(1, '/home/pi/projects/test_lcm/iust-quadruped/control/')
sys.path.insert(2, '/home/pi/projects/test_lcm/iust-quadruped/control/robot_types/')

import lcm

from robot_types import IMU_t


lc = lcm.LCM()
resp = IMU_t()

ser = serial.Serial('/dev/ttyACM0', 2000000)
ser.reset_input_buffer()
print("IMU ready.")

flag=0
while True :
    time.sleep(0.0008)
    try:
        while(flag==0):
            if ser.read()==b'\n':
                flag+=1
                break

        if ser.in_waiting > 0:
            data = ser.readline()

        try:
            acc_x, acc_y, acc_z = map(float, str(data)[2:-4].lstrip().replace("  ", " ").split(" "))
            resp.acc_x = acc_x
            resp.acc_y = acc_y
            resp.acc_z = acc_z

            lc.publish("IMU_ACC", resp.encode())

        except Exception as e:
            print("error!")
            if len(data) != 0:
                print(str(data[-1]))
            else:
                print("empty data recieved!")
            print(e)
            pass

    except KeyboardInterrupt:
        print("program closed manually!")
        sys.exit(1)