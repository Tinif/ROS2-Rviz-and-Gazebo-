from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch.substitutions import Command
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    urdf_path=os.path.join(get_package_share_directory('robot_1py'),'urdf','bot_1.urdf.xacro')
    robot_desp=ParameterValue(Command(['xacro ',urdf_path]),value_type=str)

    robot_state_pub_node=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description':robot_desp}]
    )

    joint_state_pub_node=Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"

    )

    rviz_nod= Node(
        package="rviz2",
        executable="rviz2",
        arguments=[ '-d',str("/home/asus/z2_udemy/src/robot_1py/config/robo.rviz") ]
    )

    return LaunchDescription([
        robot_state_pub_node,
        joint_state_pub_node,
        rviz_nod
    ])