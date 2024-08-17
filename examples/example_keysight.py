import time

from cc.scpi import Keysight81134A

device = Keysight81134A("128.32.62.102")
device.connect()

print(device.get_instrument_identification())


device.enable_output(Keysight81134A.Channel.CH1)
device.disable_output(Keysight81134A.Channel.CH1)