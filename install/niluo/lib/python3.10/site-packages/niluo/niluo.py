import rclpy
from rclpy.node import Node
from std_msgs.msg import String,UInt32

class NiluoNode(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info(f"大家好，我是{name}")
        self.shangclass=self.create_publisher(String,"mingyue",10)

        self.i=0
        timer_period=5
        self.timer=self.create_timer(timer_period,self.timer_callback)

        self.boat=5
        self.getboat=self.create_subscription(UInt32,"makeboat",self.makeboat_callback,10)

    def timer_callback(self):
        msg=String()
        msg.data=f"第{self.i}次上工程设计课"
        self.shangclass.publish(msg)
        self.get_logger().info(f"罗の课：{msg.data}")
        self.i+=1

    def makeboat_callback(self,boat):
        self.boat+=boat.data
        self.get_logger().info(f"罗の课：我们做的船负重增加到{self.boat}!")

def main(args=None):
    rclpy.init(args=args)
    node=NiluoNode("niluo")
    rclpy.spin(node)
    rclpy.shutdown()
