import sys
import lcm

from bisect import bisect_left, bisect, bisect_right

sys.path.insert(1, '/home/pi/projects/test_lcm/iust-quadruped/control/')
sys.path.insert(2, '/home/pi/projects/test_lcm/iust-quadruped/control/robot_types/')

from robot_types import IMU_t, contact_t, motor_response_t


def find_closest(myList, myNumber):
    # use binary search to find closest number in the list
    pos = bisect(myList, myNumber)
    if pos == 0:
        return 0
    if pos == len(myList):
        return len(myList)-1
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
        return pos
    else:
        return pos-1

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
    if event.channel == "MOTOR_RESPONSE":
        msg = motor_response_t.decode(event.data)

        data_motor_p[str(int(msg.id))].append(msg.p)
        motor_timestamp[str(int(msg.id))].append(event.timestamp/1000)

    elif event.channel == "IMU_ACC" and (sys.argv[2] == '0' or sys.argv[2] == '2'):
        msg = IMU_t.decode(event.data)

        data_acc_x.append(msg.acc_x)
        data_acc_y.append(msg.acc_y)
        data_acc_z.append(msg.acc_z)
        imu_timestamp.append(event.timestamp/1000)

    elif event.channel == "CONTACT" and (sys.argv[2] == '0' or sys.argv[2] == '3'):
        msg = contact_t.decode(event.data)

        contact_timestamp.append(event.timestamp/1000)
        contact_data.append(msg.touch)

start_time = contact_timestamp[0]
contact_timestamp = [x-start_time for x in contact_timestamp]
imu_timestamp = [x-start_time for x in imu_timestamp]
motor_timestamp["1"] = [x-start_time for x in motor_timestamp["1"]]
motor_timestamp["2"] = [x-start_time for x in motor_timestamp["2"]]
motor_timestamp["5"] = [x-start_time for x in motor_timestamp["5"]]

for i in range(len(imu_timestamp)):
        matched_idx.append(find_closest(contact_timestamp, imu_timestamp[i]))

for i in range(len(imu_timestamp)):
    print("imu:", imu_timestamp[i])
    print("contact", contact_timestamp[matched_idx[i]])
