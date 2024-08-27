import sys

from custom_interface.srv import GetPosition
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(GetPosition, 'get_position_aibo')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = GetPosition.Request()

    def send_request(self, a, b, c, d,e):
        self.req.th1 = float(a)
        self.req.th2 = float(b)
        self.req.th3 = float(c)
        self.req.l1 = float(d)
        self.req.l2 = float(e)

        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    future = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),int(sys.argv[5]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        'Result of add_thee_ints: for %d  %d  %d  %d %d %d %d %d' %
        (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),int(sys.argv[5]), response.x, response.y, response.z))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()