import sys

import lcm

sys.path.insert(1, '../lcm_types')
sys.path.insert(2, '../lcm_types/python')

from lcm_types.python import example_t

# setup msg
msg = example_t()
msg.counter = 1

# assign udp multicast
t = "udpm://224.0.55.55:5001?ttl=255"
lc = lcm.LCM(t)
lc.publish("EXAMPLE", msg.encode())