import sys
import argparse

import lcm
import matplotlib.pyplot as plt

sys.path.insert(1, './lcm_types')
sys.path.insert(2, './lcm_types/python')

from lcm_types.python import contact_t, motor_response_t, IMU_t


parser = argparse.ArgumentParser(description="reads the recorded logs of actuators and other sensors and shows simple graph of the outputs.")

parser.add_argument("-m", "--Motor", action="store_true", help="Shows logs of Motors")
parser.add_argument("-i", "--Imu", action="store_true", help="Shows logs of IMU")
parser.add_argument("-c", "--Contact", action="store_true", help="Shows logs of Contact sensor")
parser.add_argument("-a", "--All", action="store_true", help="Shows all types of output")
parser.add_argument("-f", "--File", type=argparse.FileType('r'), help="LCM log file path")
parser.add_argument("-p", "--Plot", action="store_true", help="Plot the selected data")
parser.add_argument("-t", "--Terminal", action="store_true", help="show the outputs in terminal")
args = parser.parse_args()

try:
    options = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

log = lcm.EventLog(args.File.name, "r")

contact_data = []
contact_timestamp = []

data_acc_x = []
data_acc_y = []
data_acc_z = []
imu_timestamp = []

# keys are the actuator id
data_motor_p = {"1":[], "2":[], "5":[]}
motor_timestamp = {"1":[], "2":[], "5":[]}

for event in log:
    if (args.All or args.Motor) and event.channel == "MOTOR_RESPONSE":
        msg = motor_response_t.decode(event.data)

        data_motor_p[str(int(msg.id))].append(msg.p)
        motor_timestamp[str(int(msg.id))].append(event.timestamp/1000)

        if args.terminal:
            print("motor data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   id       = %s" % str(msg.id))
            print("   p        = %s" % str(msg.p))
            print("   v        = %s" % str(msg.v))
            print("   i        = %s" % str(msg.i))
            print("")


    elif (args.All or args.Imu) and event.channel == "IMU_ACC":
        msg = IMU_t.decode(event.data)

        data_acc_x.append(msg.acc_x)
        data_acc_y.append(msg.acc_y)
        data_acc_z.append(msg.acc_z)
        imu_timestamp.append(event.timestamp/1000)

        if args.terminal:
            print("imu data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   acc_x       = %s" % str(msg.acc_x))
            print("   acc_y       = %s" % str(msg.acc_y))
            print("   acc_z       = %s" % str(msg.acc_z))
            print("")

    elif (args.All or args.Imu) and event.channel == "CONTACT":
        msg = contact_t.decode(event.data)

        contact_timestamp.append(event.timestamp/1000)
        contact_data.append(msg.touch)

        if args.terminal:
            print("contact data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   touch       = %s" % str(msg.touch))
            print("")

if args.Plot:
    # set initial time to first contact sensor timestamp.
    start_time = contact_timestamp[0]
    contact_timestamp = [x-start_time for x in contact_timestamp]
    imu_timestamp = [x-start_time for x in imu_timestamp]
    motor_timestamp["1"] = [x-start_time for x in motor_timestamp["1"]]
    motor_timestamp["2"] = [x-start_time for x in motor_timestamp["2"]]
    motor_timestamp["5"] = [x-start_time for x in motor_timestamp["5"]]

    print("plot!")

    plt.figure()
    plt.plot(contact_timestamp, contact_data)
    plt.plot(imu_timestamp, data_acc_x)
    plt.plot(imu_timestamp, data_acc_y)
    plt.plot(imu_timestamp, data_acc_z)
    plt.plot(motor_timestamp["1"], data_motor_p["1"])
    plt.plot(motor_timestamp["2"], data_motor_p["2"])
    plt.plot(motor_timestamp["5"], data_motor_p["5"])
    plt.show()