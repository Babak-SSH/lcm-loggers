import sys
import lcm
import matplotlib.pyplot as plt

sys.path.insert(1, '/home/pi/projects/test_lcm/iust-quadruped/control/')
sys.path.insert(2, '/home/pi/projects/test_lcm/iust-quadruped/control/robot_types/')

from robot_types import IMU_t, contact_t, motor_response_t

if len(sys.argv) < 2:
    sys.stderr.write("usage: read-log <logfile>\n")
    sys.exit(1)

log = lcm.EventLog(sys.argv[1], "r")

contact_data = []
contact_timestamp = []

data_acc_x = []
data_acc_y = []
data_acc_z = []
imu_timestamp = []

data_motor_p = {"1":[], "2":[], "5":[]}
motor_timestamp = {"1":[], "2":[], "5":[]}

for event in log:
    if event.channel == "MOTOR_RESPONSE" and (sys.argv[2] == '0' or sys.argv[2] == '1'):
        msg = motor_response_t.decode(event.data)

        data_motor_p[str(int(msg.id))].append(msg.p)
        motor_timestamp[str(int(msg.id))].append(event.timestamp/1000)

        if sys.argv[3] == "t":
            print("motor data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   id       = %s" % str(msg.id))
            print("   p        = %s" % str(msg.p))
            print("   v        = %s" % str(msg.v))
            print("   i        = %s" % str(msg.i))
            print("")


    elif event.channel == "IMU_ACC" and (sys.argv[2] == '0' or sys.argv[2] == '2'):
        msg = IMU_t.decode(event.data)

        data_acc_x.append(msg.acc_x)
        data_acc_y.append(msg.acc_y)
        data_acc_z.append(msg.acc_z)
        imu_timestamp.append(event.timestamp/1000)

        if sys.argv[3] == "t":
            print("imu data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   acc_x       = %s" % str(msg.acc_x))
            print("   acc_y       = %s" % str(msg.acc_y))
            print("   acc_z       = %s" % str(msg.acc_z))
            print("")

    elif event.channel == "CONTACT" and (sys.argv[2] == '0' or sys.argv[2] == '3'):
        msg = contact_t.decode(event.data)

        contact_timestamp.append(event.timestamp/1000)
        contact_data.append(msg.touch)

        if sys.argv[3] == "t":
            print("contact data:")
            print("   timestamp   = %s" % str(event.timestamp/1000))
            print("   touch       = %s" % str(msg.touch))
            print("")

if sys.argv[3] == "plot":
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

