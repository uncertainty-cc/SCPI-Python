
from .generic_instrument import GenericInstrument

class SiglentSPD3303X(GenericInstrument):
    class Channel:
        CH1 = "CH1"
        CH2 = "CH2"
    
    def getCurrent(self, channel):
        return float(self.query("MEASURE:CURRENT? {ch}".format(ch=channel)))
    
    def getVoltage(self, channel):
        return float(self.query("MEASURE:VOLTAGE? {ch}".format(ch=channel)))
    
    def getPower(self, channel):
        return float(self.query("MEASURE:POWER? {ch}".format(ch=channel)))
    
    def setCurrent(self, value, channel):
        self.command("{ch}:CURRENT {val}".format(ch=channel, val=value))
        
    def setVoltage(self, value, channel):
        self.command("{ch}:VOLTAGE {val}".format(ch=channel, val=value))

    def disableOutput(self, channel):
        self.command("OUTPUT {ch},OFF".format(ch=channel))

    def enableOutput(self, channel):
        self.command("OUTPUT {ch},ON".format(ch=channel))