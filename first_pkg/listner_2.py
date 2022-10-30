import rclpy
from rclpy.node import Node 
from std_msgs.msg import String

class Listner(Node):
    def __init__(self):
            super().__init__("listner")
            self.sub=self.create_subscription(String,'chat',self.call_back_function,10)  
        
    def call_back_function(self,data):
        self.get_logger().info(f"talker 3 {data.data}")
def main(args=None):
    rclpy.init(args=args)
    node=Listner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()