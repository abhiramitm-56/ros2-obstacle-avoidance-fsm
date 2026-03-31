import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class ObstacleAvoidance(Node):

    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Subscriber to LiDAR
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        # Publisher for movement
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Initial state
        self.state = "FORWARD"

        # Thresholds
        self.safe_distance = 0.5
        self.danger_distance = 0.2

    def scan_callback(self, msg):

        # Filter front LiDAR data
        front_ranges = msg.ranges[0:30] + msg.ranges[-30:]

        # Remove invalid values (inf, nan)
        valid_ranges = [r for r in front_ranges if not math.isinf(r) and not math.isnan(r)]

        if len(valid_ranges) == 0:
            return

        min_distance = min(valid_ranges)

        cmd = Twist()

        # FSM Logic
        if min_distance > self.safe_distance:
            self.state = "FORWARD"
        elif min_distance > self.danger_distance:
            self.state = "TURN"
        else:
            self.state = "STOP"

        # Actions
        if self.state == "FORWARD":
            cmd.linear.x = 0.2
            cmd.angular.z = 0.0

        elif self.state == "TURN":
            cmd.linear.x = 0.0
            cmd.angular.z = 0.5

        elif self.state == "STOP":
            cmd.linear.x = 0.0
            cmd.angular.z = 0.0

        # Publish command
        self.publisher.publish(cmd)

        # Debug log
        self.get_logger().info(
            f"State: {self.state}, Distance: {min_distance:.2f}"
        )


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
