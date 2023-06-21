import os
import sys
import pathlib
from launch import LaunchDescription
from launch_ros.actions import Node
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
from launchhelp import LaunchHelper

def generate_launch_description():    
    launch_helper = LaunchHelper()

    # launch_helper.add_node_launch("phoenixpro_control_node", "phoenixpro_control_node.yaml")
    launch_helper.add_node_launch("hmi_agent_ros2_sample_node", "hmi_agent_ros2_sample_node.yaml")
    
    return launch_helper.get_launch_description()