import time

from cc.scpi import Keysight81134A

device = Keysight81134A("128.32.62.102")
device.connect()

print(device.getInstrumentIdentification())


device.enableOutput(Keysight81134A.Channel.CH1)
device.disableOutput(Keysight81134A.Channel.CH1)