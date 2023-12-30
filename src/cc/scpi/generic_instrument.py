import socket
import time

from cc.serializer import SocketSerializer

class GenericInstrument:
    """
    Generic instrument class.
    """
    
    def __init__(self, ip_address, port=5025):
        self.s = None
        self.ip_address = ip_address
        self.port = port
    
    def connect(self):
        """
        Connect to the instrument.
        """
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        addr = (self.ip_address, self.port)
        try:
            self.s.connect(addr)
        except socket.error as e:
            print("failed to connect: ", addr)
            print(e)
        
        return self.s

    def close(self):
        """
        Close the connection.
        """
        self.s.close()
    
    def command(self, cmd: str):
        """
        Send a command to the instrument.
        
        Args:
            cmd: the command to send
        """
        ser = SocketSerializer(self.s, buffered_transmit=True)
        ser.transmit(cmd.encode())
    
    def query(self, cmd: str):
        """
        Send a query to the instrument.

        Args:
            cmd: the command to send
        
        Returns:
            the response from the instrument
        """
        ser = SocketSerializer(self.s, buffered_transmit=True)
        ser.transmit(cmd.encode())
        data = ser.receive()
        return data.decode()

    def getIDN(self):
        """
        Get the instrument identification number

        Returns:
            the instrument identification
        """
        return self.query("*IDN?")

    def getInstrumentIdentification(self):
        """
        Get the instrument identification number. This is an alias for `getIDN()`.

        Returns:
            the instrument identification
        """
        return self.getIDN()
    
