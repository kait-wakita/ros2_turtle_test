# -*- codeing: utf-8 -*-
#
# ROS action example
#

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtlesim.action import RotateAbsolute

class RotateTurtle(Node):
    def __init__(self):
        super().__init__('rotate_move')
        self._action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

    def send_goal(self, theta):
         goal_msg = RotateAbsolute.Goal()
         goal_msg.theta = theta
         self._action_client.wait_for_server()
         self._action_client.send_goal_async(goal_msg)

def main(args=None):
    rclpy.init(args=args)
    action_client = RotateTurtle()
    theta = 0.0
    action_client.send_goal(theta)

if __name__ == '__main__':
    main()


