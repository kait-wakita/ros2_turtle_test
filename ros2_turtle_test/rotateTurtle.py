# -*- codeing: utf-8 -*-
#
# ROS action example
#

import rclpy, time, random
from rclpy.node import Node
from rclpy.action import ActionClient
from turtlesim.action import RotateAbsolute

class RotateTurtle(Node):
    def __init__(self):
        super().__init__('rotate_turtle')
        self._action_client = ActionClient(self, RotateAbsolute, '/turtle1/rotate_absolute')

    def send_goals(self,theta):
         self.theta = theta
         goal_msg = RotateAbsolute.Goal()
         while rclpy.ok():
             #self.theta = self.theta + 1.57
             sleep_duration = random.random()*5.0
             target_angle = random.random()*6.28-3.14
             goal_msg.theta = target_angle

             self._action_client.wait_for_server()
             self._action_client.send_goal_async(goal_msg)
             self.get_logger().info('target=%4.0f(deg),sleep%3.1f(sec)' % (target_angle*180/3.14, sleep_duration))
             time.sleep(sleep_duration)

         rclpy.shutdown()
         
         
def main(args=None):
    rclpy.init(args=args)
    action_client = RotateTurtle()
    action_client.send_goals(0.0)
    
if __name__ == '__main__':
    main()

