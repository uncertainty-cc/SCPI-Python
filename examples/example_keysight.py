import time

from cc.scpi.keysight import K81134A

device = K81134A("128.32.62.102")
device.connect()

print(device.get_instrument_identification())


device.enable_output(K81134A.Channel.CH1)
device.disable_output(K81134A.Channel.CH1)