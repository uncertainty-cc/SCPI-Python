
from .generic_instrument import GenericInstrument

class Keysight33600A(GenericInstrument):
    """
    Keysight 33600A Series Waveform Generator
    
    The Keysight 33600A Series Waveform Generator is a versatile signal generator with the capabilities of generating sine, square, ramp, pulse, and arbitrary waveforms. It can be used to test analog designs, such as filters, amplifiers, etc.
    
    https://www.keysight.com/fr/en/assets/7018-04123/data-sheets-archived/5991-3272.pdf
    """
    
    class Function:
        """
        The function of the output waveform.
        """
        SQUARE = "SQUARE"

    class Channel:
        """
        The channel of the output waveform.
        """
        CH1 = "1"
        CH2 = "2"
    
    def set_function(self, function: Function, channel: Channel):
        """
        Set function of both channels

        Args:
            function: the target function
            channel: the target channel
        """
        self.command("SOURCE{ch}:FUNCTION {func}".format(ch=channel, func=function))
    
    def set_frequency(self, value: float, channel: Channel):
        """
        Set frequency of both channels
        
        Args:
            value: the target frequency value in hertz (Hz). The value must be within [100, 600000000] Hz.
            channel: the target channel
        """
        self.command("SOURCE{ch}:FREQUENCY {val}".format(ch=channel, val=value))
    
    def set_high_voltage(self, value: float, channel: Channel):
        """
        Set the voltage level of the high state of the output waveform.

        Args:
            value: the target voltage value in volts (V).
            channel: the target channel
        """
        self.command("SOURCE{ch}:VOLTAGE:HIGH {val}".format(ch=channel, val=value))
    
    def set_low_voltage(self, value: float, channel: Channel):
        """
        Set the voltage level of the low state of the output waveform.

        Args:
            value: the target voltage value in volts (V).
            channel: the target channel
        """
        self.command("SOURCE{ch}:VOLTAGE:LOW {val}".format(ch=channel, val=value))
    
    def set_output_load(self, value: float, channel: Channel):
        """
        Set the output load impedance.

        Args:
            value: the target load value in ohms (Ω). The value must be within [1, 1000000] Ω.
            channel: the target channel
        """
        if value == float("inf"):
            value = "INFINITY"
        self.command("OUTPUT{ch}:LOAD {val}".format(ch=channel, val=value))

    def disable_output(self, channel: Channel):
        """
        Disable the output of the specified channel.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT{ch} OFF".format(ch=channel))

    def enable_output(self, channel: Channel):
        """
        Enable the output of the specified channel.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT{ch} ON".format(ch=channel))


class Keysight81134A(GenericInstrument):
    """
    Keysight 81134A Pulse Pattern Generator, Dual-Channel

    The Keysight 81134A is a dual-channel, 3.35 GHz Pulse Pattern Generator. It is used to test digital designs from DC to 3.35 GHz. It can be used to test digital interfaces, such as HDMI, MIPI, DisplayPort, SATA, USB, DDR, etc.

    https://www.keysight.com/fr/en/assets/7018-01085/data-sheets/5988-5549.pdf
    """

    class Channel:
        """
        The channel of the output waveform.
        """
        CH1 = "1"
        CH2 = "2"
    
    class Function:
        """
        The function of the output waveform.
        """
        SQUARE = "SQUARE"
        DATA = "DATA"
    
    def setFunction(self, function: Function, channel: Channel):
        """
        Set function of both channels

        Args:
            function: the target function
            channel: the target channel
        """
        self.command(":SOURCE:FUNCTION:MODE{ch} {func}".format(ch=channel, func=function))
    
    def setFrequency(self, value: int):
        """
        Set frequency of both channels

        Args:
            value: the target frequency value in Hz. The value must be within [15000000, 3350000000] Hz.
        """
        assert 15000000. <= value and value <= 3350000000.
        self.command(":FREQUENCY {val}".format(val=value))
    
    def setFrequencyDivisor(self, value: int, channel: Channel):
        """
        Set the frequency divider of both channels
        
        Args:
            value: the target frequency divider value. The value must be one of 1, 2, 4, 8, 16, 32, 64, 128
        """
        assert value in [1, 2, 4, 8, 16, 32, 64, 128], "Invalid frequency divisor"
        self.command(":OUTPUT{ch}:DIVIDER {val}".format(ch=channel, val=value))
    
    def setVoltageHigh(self, value: float, channel: Channel):
        """
        Set the voltage level of the high state of the output waveform.
        
        Args:
            value: the target voltage value in volts (V). The value must be within [0, 2] V.
            channel: the target channel
        """
        assert 0. <= value and value <= 2.
        self.command(":SOURCE:VOLTAGE{ch}:HIGH {val}V".format(ch=channel, val=value))

    def setVoltageLow(self, value: float, channel: Channel):
        """
        Set the voltage level of the high state of the output waveform.
        
        Args:
            value: the target voltage value in volts (V). The value must be within [0, 2] V.
            channel: the target channel
        """
        assert 0. <= value and value <= 2.
        self.command(":SOURCE:VOLTAGE{ch}:LOW {val}V".format(ch=channel, val=value))
    
    def disableOutput(self, channel: Channel):
        """
        Disable the output of both phases of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch} OFF".format(ch=channel))

    def disableOutputP(self, channel: Channel):
        """
        Disable the output of the positive phase of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch}:POS OFF".format(ch=channel))

    def disableOutputN(self, channel: Channel):
        """
        Disable the output of the negative phase of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch}:NEG OFF".format(ch=channel))

    def enableOutput(self, channel: Channel):
        """
        Enable the output of both phases of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch} ON".format(ch=channel))

    def enableOutputP(self, channel: Channel):
        """
        Enable the output of the positive phase of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch}:POS ON".format(ch=channel))

    def enableOutputN(self, channel: Channel):
        """
        Enable the output of the negative phase of the specified channel.

        Args:
            channel: the target channel
        """
        self.command(":OUTPUT{ch}:NEG ON".format(ch=channel))
