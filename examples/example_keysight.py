import time

from cc.scpi import KeySight33600A

device = KeySight33600A("128.32.62.101")
device.connect()

print(device.getInstrumentIdentification())
