import socket

from cc.serializer import SocketSerializer

class GenericInstrument:
    """
    Generic instrument class.
    """
    
    def __init__(self, ip_address, port=5025):
        self._sock = None
        self.ip_address = ip_address
        self.port = port
    
    def connect(self):
        """
        Connect to the instrument.
        """
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        addr = (self.ip_address, self.port)
        try:
            self._sock.connect(addr)
        except socket.error as e:
            print("failed to connect: ", addr)
            print(e)
        
        return self._sock

    def close(self):
        """
        Close the connection.
        """
        self._sock.close()
    
    def command(self, cmd: str):
        """
        Send a command to the instrument.
        
        Args:
            cmd: the command to send
        """
        ser = SocketSerializer(self._sock, buffered_transmit=True)
        ser.transmit(cmd.encode())
    
    def query(self, cmd: str):
        """
        Send a query to the instrument.

        Args:
            cmd: the command to send
        
        Returns:
            the response from the instrument
        """
        ser = SocketSerializer(self._sock, buffered_transmit=True)
        ser.transmit(cmd.encode())
        data = ser.receive()
        return data.decode()

    def get_idn(self):
        """
        Get the instrument identification number

        Returns:
            the instrument identification
        """
        return self.query("*IDN?")

    def get_instrument_identification(self):
        """
        Get the instrument identification number. This is an alias for `get_idn()`.

        Returns:
            the instrument identification
        """
        return self.get_idn()
    
