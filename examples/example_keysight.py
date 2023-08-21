import time

from cc.scpi import Keysight33600A

device = Keysight33600A("128.32.62.101")
device.connect()

print(device.getInstrumentIdentification())
