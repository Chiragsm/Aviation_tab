import serial                                           # import serial library
arduino = serial.Serial('COM3', 9600)   # create serial object named arduino
class But_comm:
        def __init__(self):
                self.command = str("90")
                arduino.write(bytes(self.command, 'utf-8'))

        def a_but(self):
                self.command = str("30")
                arduino.write(bytes(self.command, 'utf-8'))


        def c_but(self):
                self.command = str("90")
                arduino.write(bytes(self.command, 'utf-8'))


        def d_but(self):
                self.command = str("170")
                arduino.write(bytes(self.command, 'utf-8'))


        def re_but(self):
                self.command = str("0")
                arduino.write(bytes(self.command, 'utf-8'))