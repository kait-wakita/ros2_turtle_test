import launch.actions
import launch_ros.actions
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        launch.actions.LogInfo(
            msg="Launch turtlesim node and turtle_teleop_key_node."),
        launch.actions.TimerAction(period=3.0,actions=[
            launch.actions.LogInfo(
                msg="It's been three minutes scince the launch."),
            ]),
        Node(
            package='turtlesim',
            namespace='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen',
            parameters=[{'background_r':255},
                        {'background_g':255},
                        {'background_b':0},]),
        Node(
            package='turtlesim',
            namespace='turtlesim',
            executable='turtle_teleop_key',
            name='teleop_turtle',
            prefix="xterm -e"
            ),
        ])

