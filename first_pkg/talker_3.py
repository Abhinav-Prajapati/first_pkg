import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("talker_3")
        self.publish_=self.create_publisher(String,"chat",10)
        self.timer=self.create_timer(1,self.call_back_function)
        self.counter=0

    def call_back_function(self):
        msg=String()
        msg.data=f"Hello boie {self.counter} "
        self.publish_.publish(msg)
        self.get_logger().info(msg.data)
        self.counter+=1
    
def main(args=None):
    rclpy.init(args=args)

    node=MyNode()

    rclpy.spin(node)
    rclpy.shutdown()
if __name__=='__main__':
    main()