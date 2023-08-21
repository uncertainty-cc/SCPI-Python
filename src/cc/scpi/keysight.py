
from .generic_instrument import GenericInstrument

class Keysight33600A(GenericInstrument):
    class Channel:
        CH1 = "1"
        CH2 = "2"
    
    class Function:
        SQUARE = "SQUARE"
    
    def setFunction(self, function, channel):
        self.command("SOURCE{ch}:FUNCTION {func}".format(ch=channel, func=function))
    
    def setFrequency(self, value, channel):
        self.command("SOURCE{ch}:FREQUENCY {val}".format(ch=channel, val=value))
    
    def setVoltageHigh(self, value, channel):
        self.command("SOURCE{ch}:VOLTAGE:HIGH {val}".format(ch=channel, val=value))
    
    def setVoltageLow(self, value, channel):
        self.command("SOURCE{ch}:VOLTAGE:LOW {val}".format(ch=channel, val=value))
    
    def setOutputLoad(self, value, channel):
        if value == "inf":
            value = "INFINITY"
        self.command("OUTPUT{ch}:LOAD {val}".format(ch=channel, val=value))

    def disableOutput(self, channel):
        self.command("OUTPUT{ch} OFF".format(ch=channel))

    def enableOutput(self, channel):
        self.command("OUTPUT{ch} ON".format(ch=channel))
    
class Keysight81134A(GenericInstrument):
    class Channel:
        CH1 = "1"
        CH2 = "2"
    
    class Function:
        SQUARE = "SQUARE"
        DATA = "DATA"
    
    def setFunction(self, function, channel):
        self.command(":SOURCE:FUNCTION:MODE{ch} {func}".format(ch=channel, func=function))
    
    """
    @param value: need to be within [15000000, 3350000000] Hz
    """
    def setFrequency(self, value):
        assert 15000000. <= value and value <= 3350000000.
        self.command(":FREQUENCY {val}".format(val=value))
    
    """
    @param value: need to be one of 1, 2, 4, 8, 16, 32, 64, 128
    """
    def setFrequencyDivisor(self, value, channel):
        self.command(":OUTPUT{ch}:DIVIDER {val}".format(ch=channel, val=value))
    
    """
    @param value: need to be within [0, 2] V
    """
    def setVoltageHigh(self, value, channel):
        assert 0. <= value and value <= 2.
        self.command(":SOURCE:VOLTAGE{ch}:HIGH {val}V".format(ch=channel, val=value))

    """
    @param value: need to be within [0, 2] V
    """
    def setVoltageLow(self, value, channel):
        assert 0. <= value and value <= 2.
        self.command(":SOURCE:VOLTAGE{ch}:LOW {val}V".format(ch=channel, val=value))
    
    def disableOutput(self, channel):
        self.command(":OUTPUT{ch} OFF".format(ch=channel))

    def disableOutputP(self, channel):
        self.command(":OUTPUT{ch}:POS OFF".format(ch=channel))

    def disableOutputN(self, channel):
        self.command(":OUTPUT{ch}:NEG OFF".format(ch=channel))

    def enableOutput(self, channel):
        self.command(":OUTPUT{ch} ON".format(ch=channel))

    def enableOutputP(self, channel):
        self.command(":OUTPUT{ch}:POS ON".format(ch=channel))

    def enableOutputN(self, channel):
        self.command(":OUTPUT{ch}:NEG ON".format(ch=channel))
    