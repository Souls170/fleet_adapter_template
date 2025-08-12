#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NewsSubscriberStationNode(Node):
    def __init__(self):
        super().__init__("subscriber_station")
        self.subscriber = self.create_subscription(String, "robot_news", self.consume_news, 10)

    def consume_news(self, msg: String):
        self.get_logger().info("Received: " + msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = NewsSubscriberStationNode()

    # rclpy.spin() is used to keep a ROS2 node running and processing data callbacks
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()