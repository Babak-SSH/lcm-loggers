# log_data
read and log IMU and contact sensors data.

for plot output:
```bash
python3 read_log_sensors.py lcm_log_file 0 plot
```

for terminal output (n=1 motor response, 2 IMU data, 3 contact sensor):
```bash
python3 read_log_sensors.py lcm_log_file n t
```
