from custom_interface.srv import AddThreeInts

import rclpy
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv =  self.create_service(AddThreeInts, 'add_thee_ints', self.add_numbers_callback)

    def add_numbers_callback(self, req, res):
        res.sum = req.a + req.b + req.c

        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (req.a, req.b, req.c))

        return res


def main():
    rclpy.init()
    min_svc = MinimalService()
    rclpy.spin(min_svc)
    rclpy.shutdown()


if __name__ == '__main__':
    main()