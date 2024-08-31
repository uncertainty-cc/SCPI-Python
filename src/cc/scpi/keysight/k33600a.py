
from ..generic_instrument import GenericInstrument

class K33600A(GenericInstrument):
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

