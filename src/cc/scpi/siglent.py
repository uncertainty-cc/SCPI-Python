
from .generic_instrument import GenericInstrument

class SiglentSPD3303X(GenericInstrument):
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
    
    def getCurrent(self, channel: Channel):
        """
        Get the current reading of the output.

        Args:
            channel: the target channel

        Returns:
            the current reading of the output in amperes (A)
        """
        return float(self.query("MEASURE:CURRENT? {ch}".format(ch=channel)))
    
    def getVoltage(self, channel: Channel):
        """
        Get the voltage reading of the output.
        
        Args:
            channel: the target channel
        
        Returns:
            the voltage reading of the output in volts (V)
        """
        return float(self.query("MEASURE:VOLTAGE? {ch}".format(ch=channel)))
    
    def getPower(self, channel: Channel):
        """
        Get the power reading of the output.

        Args:
            channel: the target channel
        
        Returns:
            the power reading of the output in watts (W)
        """
        return float(self.query("MEASURE:POWER? {ch}".format(ch=channel)))
    
    def setCurrent(self, value: float, channel: Channel):
        """
        Set the current limit of the output.
        
        Args:
            value: the target current limit value in amperes (A)
            channel: the target channel
        """
        self.command("{ch}:CURRENT {val}".format(ch=channel, val=value))
        
    def setVoltage(self, value: float, channel: Channel):
        """
        Set the voltage of the output.

        Args:
            value: the target voltage value in volts (V)
            channel: the target channel
        """
        self.command("{ch}:VOLTAGE {val}".format(ch=channel, val=value))

    def disableOutput(self, channel: Channel):
        """
        Disable the output.
        
        Args:
            channel: the target channel
        """
        self.command("OUTPUT {ch},OFF".format(ch=channel))

    def enableOutput(self, channel: Channel):
        """
        Enable the output.

        Args:
            channel: the target channel
        """
        self.command("OUTPUT {ch},ON".format(ch=channel))