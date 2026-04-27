import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: LaserScan):
        print(f"tamanio de la lectura {len(msg.ranges)}")
        print(f"tipo de dato ranges {type(msg.ranges)}")
        print(f"tamanio minimo {min(msg.ranges)}")
        print(f"distancia frente al robot {msg.ranges[int(len(msg.ranges)/2)]}")


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()