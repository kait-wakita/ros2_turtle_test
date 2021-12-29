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
        super().__init__('rotate_turtle')
        self.theta = 0.0
        self._action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')
        self.tmr = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
         goal_msg = RotateAbsolute.Goal()
         goal_msg.theta = self.theta
         self._action_client.wait_for_server()
         self._action_client.send_goal_async(goal_msg)
         self.theta = self.theta + 1.57
         
         
def main(args=None):
    rclpy.init(args=args)
    action_client = RotateTurtle()
    rclpy.spin(action_client)
    
if __name__ == '__main__':
    main()

