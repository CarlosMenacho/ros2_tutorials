import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class RobotMove(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        timer_period = 0.2  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = TwistStamped()

        msg.header.frame_id = ""
        msg.header.stamp = self.get_clock().now().to_msg()

        msg.twist.linear.x = 0.2
        msg.twist.angular.z = 0.01

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = RobotMove()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()