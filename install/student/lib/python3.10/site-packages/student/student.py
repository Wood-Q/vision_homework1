import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32

class StudentNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info(f"我是明月班的学生{name}")

        self.niumaboat=self.create_publisher(UInt32,"makeboat",10)

        self.shangke=self.create_subscription(String,"mingyue",self.mingyue_callback,10)
    
    def mingyue_callback(self,boat):
        boat=UInt32()
        boat.data=1

        self.niumaboat.publish(boat)

        self.get_logger().info(f"我上了课，我要多做{boat.data}kg船！")

def main(args=None):
    rclpy.init(args=args)
    node=StudentNode("waya")
    rclpy.spin(node)
    rclpy.shutdown()