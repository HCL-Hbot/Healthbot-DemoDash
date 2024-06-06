from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort

class SerialComm:

    def __init__(self):
        self.serial = QSerialPort()
        self.set_port_name("COM14")  # Default port name
        self.serial.setBaudRate(QSerialPort.Baud115200)  # Adjust baud rate as needed
        self.serial.setDataBits(QSerialPort.Data8)
        self.serial.setParity(QSerialPort.NoParity)
        self.serial.setStopBits(QSerialPort.OneStop)
        self.serial.setFlowControl(QSerialPort.NoFlowControl)

    def set_port_name(self, port_name):
        if self.serial.isOpen():
            self.serial.close()
        self.serial.setPortName(port_name)
        self.open_port()

    def open_port(self):
        if not self.serial.isOpen():
            if self.serial.open(QIODevice.ReadWrite):
                print(f"Connected to {self.serial.portName()}")
            else:
                print(f"Failed to connect to {self.serial.portName()}")

    def send(self, message: str):
        if self.serial.isOpen():
            self.serial.write(message.encode())
        else:
            print("Serial port not open")
            self.open_port()  # Try to reopen the port
            if self.serial.isOpen():
                self.serial.write(message.encode())
