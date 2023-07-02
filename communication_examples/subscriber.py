import sys

import lcm

sys.path.insert(1, '../lcm_types')
sys.path.insert(2, '../lcm_types/python')

from lcm_types.python import example_t

def my_handler(channel, data):
    msg = example_t.decode(data)
    print("   counter     = %s" % str(msg.counter))
    print("")

t = "udpm://224.0.55.55:5001?ttl=255"
lc = lcm.LCM(t)
subscription = lc.subscribe("EXAMPLE", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass
