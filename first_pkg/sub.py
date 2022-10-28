from std_msgs.msg import String
import rclpy
from rclpy.node import Node 

class Sub(Node):
    def __init__(self):
        super().__init__("listner")
        self.subscription=self.create_subscription(String,"line",self.call_back_function,10)
    def call_back_function(self,str):
        self.get_logger().info(f"Massage recived {str.data}")

def main(args=None):
    rclpy.init(args=args)
    node=Sub()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()