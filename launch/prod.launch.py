import os
import sys
import pathlib
from launch import LaunchDescription
from launch_ros.actions import Node
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
from launchhelp import LaunchHelper

def generate_launch_description():    
    launch_helper = LaunchHelper()

    launch_helper.add_node_launch("logger_ros2_node", "logger_ros2_node.yaml")
    launch_helper.add_node_launch("phoenixpro_control_node", "phoenixpro_control_node.yaml")
    launch_helper.add_node_launch("rio_control_ros2_node", "rio_control_ros2_node.yaml")
    
    return launch_helper.get_launch_description()