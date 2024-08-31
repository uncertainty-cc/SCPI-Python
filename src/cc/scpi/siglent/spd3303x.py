
from ..generic_instrument import GenericInstrument

class SPD3303X(GenericInstrument):
    """
    Siglent SPD3303X Programmable DC Power Supply

    The Siglent SPD3303X Programmable DC Power Supply is a versatile power supply with the capabilities of generating constant voltage and constant current. 

    https://siglentna.com/power-supplies/spd3303x-spd3303x-e-series-programmable-dc-power-supply/    
    """
    
    class Channel:
        """
        The channel of the output.
        """
        CH1 = "CH1"
        CH2 = "CH2"
    
    def get_current(self, channel: Channel) -> float:
        """
        Get the current reading of the output.

        Args:
            channel: the target channel

        Returns:
            the current reading of the output in amperes (A)
        """
        return float(self.query("MEASURE:CURRENT? {ch}".format(ch=channel)))
    
    def get_voltage(self, channel: Channel) -> float:
        """
        Get the voltage reading of the output.
        
        Args:
            channel: the target channel
        
        Returns:
            the voltage reading of the output in volts (V)
        """
        return float(self.query("MEASURE:VOLTAGE? {ch}".format(ch=channel)))
    
    def get_power(self, channel: Channel) -> float:
        """
        Get the power reading of the output.

        Args:
            channel: the target channel
        
        Returns:
            the power reading of the output in watts (W)
        """
        return float(self.query("MEASURE:POWER? {ch}".format(ch=channel)))
    
    def set_current(self, value: float, channel: Channel) -> None:
        """
        Set the current limit of the output.
        
        Args:
            value: the target current limit value in amperes (A)
            channel: the target channel
        """
        self.command("{ch}:CURRENT {val}".format(ch=channel, val=value))
        
    def set_voltage(self, value: float, channel: Channel) -> None:
        """
        Set the voltage of the output.

        Args:
            value: the target voltage value in volts (V)
            channel: the target channel
        """
        self.command("{ch}:VOLTAGE {val}".format(ch=channel, val=value))

    def disable_output(self, channel: Channel) -> None:
        """
        Disable the output.
        
        Args:
            channel: the target channel
        """
        self.command("OUTPUT {ch},OFF".format(ch=channel))

    def enable_output(self, channel: Channel) -> None:
        """
        Enable the output.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT {ch},ON".format(ch=channel))