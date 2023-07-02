# Log data
read and log Actuators ,IMU, contact sensors data made for robotic lab.

files related to reading sensors with rasp GPIO and serial -> [contact](./read_sensor/read_contact.py) 
-[imu](./read_sensor/read_imu.py)

to read the lcm logs from sensors:

python:
```python3
python read_log_sensors.py -h #for more info about the command
```
to compile the cpp version:
```cpp
g++ read_log_sensors.cpp -llcm -o read_log_sensors

./read_log_sensors
```

there are some simple examples to work with lcm in communication_examples.

to add new datatypes, add the lcm types to lcm_types and use lcm-gen to generate them.

to setup UDP multicast on your device run these commands:
```shell
sudo ifconfig "interface_name" multicast  
sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev "interface_name"
```