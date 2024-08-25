import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self) :
        super().__init__('PubNode')
        self.publisher = self.create_publisher(String, 'myTopic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello Class %d'% self.i
        self.publisher.publish(msg)
        self.get_logger().info('Publicando "%s"'%msg.data)
        self.i += 1

def main(args = None):
    rclpy.init(args=args)
    minimal_pub = MinimalPublisher()
    rclpy.spin(minimal_pub)

    minimal_pub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
