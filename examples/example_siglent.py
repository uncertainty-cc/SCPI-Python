import time

from cc.scpi import SiglentSPD3303X

device = SiglentSPD3303X("128.32.62.100")
device.connect()

print(device.get_instrument_identification())

device.set_voltage(0.1, device.Channel.CH1)
device.enable_output(device.Channel.CH1)

time.sleep(1)

print(device.get_voltage(device.Channel.CH1))
print(device.get_current(device.Channel.CH1))
print(device.get_power(device.Channel.CH1))


device.disable_output(device.Channel.CH1)

