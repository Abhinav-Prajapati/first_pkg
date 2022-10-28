from datetime import timedelta
from tokenize import String
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class Talker_node(Node):
    def __init__(self):
        super().__init__("Talker")
        self.pub=self.create_publisher(String,"msg_line",10)

        time_delay=1# set time delay of functoin call to 1 second
        self.New_timer=self.create_timer(time_delay,self.call_back_function)
    def call_back_function(self):
        msg=String()
        msg.data="ths is led sig"
        self.pub.publish(msg)
        self.get_logger().info(f"publishing {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node=Talker_node()

    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()

