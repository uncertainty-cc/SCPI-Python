import socket
import time

from cc.serializer import SocketSerializer

class GenericInstrument:
    def __init__(self, ip_address):
        self.s = None
        self.ip_address = ip_address
        self.port = 5025
    
    def connect(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        addr = (self.ip_address, self.port)
        try:
            self.s.connect(addr)
        except socket.error as e:
            print("failed to connect: ", addr)
            print(e)
        
        return self.s

    def close(self):
        self.s.close()
    
    def command(self, cmd):
        ser = SocketSerializer(self.s, buffered_transmit=True)
        ser.transmit(cmd.encode())
    
    def query(self, cmd):
        ser = SocketSerializer(self.s, buffered_transmit=True)
        ser.transmit(cmd.encode())
        data = ser.receive()
        return data.decode()

    def getIDN(self):
        return self.query("*IDN?")

    def getInstrumentIdentification(self):
        return self.getIDN()
    
