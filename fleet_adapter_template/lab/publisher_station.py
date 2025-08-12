#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class NewsPublishStationNode(Node):
    def __init__(self):
        super().__init__("publish_station")
        self.publisher = self.create_publisher(String, "robot_news", 10)

        # run publish news function every 0.5 seconds
        self.timer = self.create_timer(0.5, self.publish_news)

        # logger
        self.get_logger().info("Publish Station Started!")

    def publish_news(self):
        msg = String()
        msg.data = "Hello, this is a news"
        self.publisher.publish(msg)
        self.get_logger().info("Publishing: " + msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = NewsPublishStationNode()

    # rclpy.spin() is used to keep a ROS2 noe running and processing data callbacks
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
