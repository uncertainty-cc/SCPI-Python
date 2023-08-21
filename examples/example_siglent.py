import time

from cc.scpi import SiglentSPD3303X

device = SiglentSPD3303X("128.32.62.100")
device.connect()

print(device.getInstrumentIdentification())

device.setVoltage(0.1, device.Channel.CH1)
device.enableOutput(device.Channel.CH1)

time.sleep(1)

print(device.getVoltage(device.Channel.CH1))
print(device.getCurrent(device.Channel.CH1))
print(device.getPower(device.Channel.CH1))


device.disableOutput(device.Channel.CH1)

