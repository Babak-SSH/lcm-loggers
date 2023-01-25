import serial
import time
import sys

import lcm

from data_types import IMU_t

# initializing lcm and IMU_t data type
lc = lcm.LCM()
resp = IMU_t()

# initializing serial communication between rpi and arduino (ttyACM0 is serial device name for Arduino)
ser = serial.Serial('/dev/ttyACM0', 2000000)
# flushing input buffer
ser.reset_input_buffer()
print("IMU ready!")

while True :
    try:
        # data rate is about 5khz, with this sleep we reduce it to 1khz so we data every one milisecond
        time.sleep(0.0008)
        if ser.in_waiting > 0:
            data = ser.readline()

            try:
                # removing whitespaces and spliting the numbers
                acc_x, acc_y, acc_z = map(float, str(data)[2:-4].lstrip().replace("  ", " ").split(" "))
                resp.acc_x = acc_x
                resp.acc_y = acc_y
                resp.acc_z = acc_z

                # publish response data to lcm
                lc.publish("IMU_ACC", resp.encode())

            except Exception as e:
                print("IMU Error!")
                if len(data) != 0:
                    print(str(data[-1]))
                else:
                    print("Empty data recieved!")
                print(e)
                pass

    except KeyboardInterrupt:
        print("IMU closed manually!")
        sys.exit()