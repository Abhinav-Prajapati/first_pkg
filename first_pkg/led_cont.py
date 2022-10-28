import rclpy
import serial
from rclpy.node import Node

class Led_control(Node):
    def __init__(self):
        super().__init__("Read_serial")
        self.timer=self.create_timer(.1,self.read_)
    def read_(self):
        with serial.Serial('/dev/ttyACM0', 9600, timeout=1) as ser:
            line = ser.readline()   # read a '\n' terminated line
            self.get_logger().info(f"{line}")

def main(args=None):
    rclpy.init(args=args)
    cl=Led_control()
    rclpy.spin(cl)
    rclpy.shutdown()

if __name__=="__main__":
    main()

