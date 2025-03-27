import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point
import numpy as np


class InverseKinematics(Node):

    def __init__(self):
        super().__init__('inverse_kinematics')
        self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.target_sub = self.create_subscription(Point, 'target_position',
                                                   self.target_callback, 10)

        # Initial joint angles
        self.q = np.array([-0.22, 0.7, 0.03])  # [q1, q2, q3]

        # Robot link lengths
        self.l1 = 1.0
        self.l2 = 1.0
        self.l3 = 1.0

        self.timer = self.create_timer(0.1, self.update_joints)
        self.target_pos = np.array([1.0, 1.0, 0.0])  # Default target

    def forward_kinematics(self, q):
        q1, q2, q3 = q
        x = self.l2 * np.cos(q2) + self.l3 * np.cos(q2 + q3)
        y = self.l2 * np.sin(q2) + self.l3 * np.sin(q2 + q3)
        z = self.l1 + 0  # Assuming fixed height at l1
        return np.array([x, y, z])

    def jacobian(self, q):
        q1, q2, q3 = q

        # Compute partial derivatives
        j11 = 0
        j12 = -self.l2 * np.sin(q2) - self.l3 * np.sin(q2 + q3)
        j13 = -self.l3 * np.sin(q2 + q3)

        j21 = 0
        j22 = self.l2 * np.cos(q2) + self.l3 * np.cos(q2 + q3)
        j23 = self.l3 * np.cos(q2 + q3)

        j31 = 1  # Rotation along z-axis (torsional joint)
        j32 = 0
        j33 = 0

        return np.array([[j11, j12, j13], [j21, j22, j23], [j31, j32, j33]])

    def target_callback(self, msg):
        self.target_pos = np.array([msg.x, msg.y, msg.z])

    def update_joints(self):
        current_pos = self.forward_kinematics(self.q)
        error = self.target_pos - current_pos

        if np.linalg.norm(error) > 0.01:
            J = self.jacobian(self.q)
            J_pseudo_inv = np.linalg.pinv(J)  # Compute pseudo-inverse
            dq = J_pseudo_inv @ error  # Compute joint velocity update
            self.q += dq * 0.1  # Apply update with step size

        # Publish updated joint states
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['q1', 'q2', 'q3']
        msg.position = self.q.tolist()
        print("position: ", msg.position)
        self.joint_pub.publish(msg)


def main():
    rclpy.init()
    node = InverseKinematics()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
