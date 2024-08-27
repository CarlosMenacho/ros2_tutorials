from custom_interface.srv import GetPosition

import rclpy
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv =  self.create_service(GetPosition, 'get_position_aibo', self.get_pos_callback)

    def get_pos_callback(self, req, res):
        print(req.th1 + req.th2 + req.th3 + req.l1 + req.l2)

        res.x = float(1)
        res.y = float(2)
        res.z = float(3)
        # self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (req.th1, req.b, req.c))

        return res


def main():
    rclpy.init()
    min_svc = MinimalService()
    rclpy.spin(min_svc)
    rclpy.shutdown()


if __name__ == '__main__':
    main()