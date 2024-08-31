
from ..generic_instrument import GenericInstrument

class EDU36311A(GenericInstrument):
    """
    Keysight 36311A Series Smart Bench Essentials DC Power Supply
    
    The Keysight EDU36311A is a triple-output DC bench power supply rated at 90 W. 
    
    https://www.keysight.com/us/en/assets/3121-1003/data-sheets/EDU36311A-Triple-Output-Bench-Power-Supply.pdf
    """
    
    class Channel:
        """
        The channel of the output.
        """
        CH1 = "1"       # the P6V channel
        CH2 = "2"       # the P30V channel
        CH3 = "3"       # the N30V channel
    
    def get_voltage(self, channel: Channel):
        """
        Get the voltage reading of the output.

        Args:
            channel: the target channel
        """
        reading = self.query("MEASURE:VOLT? (@{ch})".format(ch=channel))
        reading = float(reading)
        return reading
    
    def get_current(self, channel: Channel):
        """
        Get the current reading of the output.

        Args:
            channel: the target channel
        """
        reading = self.query("MEASURE:CURR? (@{ch})".format(ch=channel))
        reading = float(reading)
        return reading

    def get_power(self, channel: Channel):
        """
        Get the power reading of the output.

        Args:
            channel: the target channel
        """
        voltage = self.get_voltage(channel)
        current = self.get_current(channel)
        power = voltage * current
        return power
    
    def set_voltage(self, value: float, channel: Channel):
        """
        Set the output voltage level of the specified channel.

        Args:
            value: the target voltage value in volts (V).
            channel: the target channel
        """
        self.command("VOLT {val},(@{ch})".format(ch=channel, val=value))
    
    def set_current(self, value: float, channel: Channel):
        """
        Set the output current limit of the specified channel.

        Args:
            value: the target current value in amperes (A).
            channel: the target channel
        """
        self.command("CURR {val},(@{ch})".format(ch=channel, val=value))
    
    def disable_output(self, channel: Channel):
        """
        Disable the output of the specified channel.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT OFF,(@{ch})".format(ch=channel))

    def enable_output(self, channel: Channel):
        """
        Enable the output of the specified channel.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT ON,(@{ch})".format(ch=channel))

