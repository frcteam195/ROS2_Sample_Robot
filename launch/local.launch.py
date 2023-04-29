import os
import pathlib
from launch import LaunchDescription
from launch_ros.actions import Node

class LaunchHelper:
    def __init__(self) -> None:
        self.ld = LaunchDescription()
        self.config_base_bath = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "config")

    def add_node_launch(self, node_name : str, *config_paths):
        config_list = []
        for p in config_paths:
            if isinstance(p, str):
                config_list.append(os.path.join(self.config_base_bath, p))

        self.ld.add_action(
            Node(
                package=node_name,
                name=node_name,
                executable=node_name,
                parameters=config_list
            )
        )

    def get_launch_description(self):
        return self.ld


def generate_launch_description():    
    launch_helper = LaunchHelper()

    launch_helper.add_node_launch("phoenixpro_control_node", "phoenixpro_control_node.yaml")
    
    return launch_helper.get_launch_description()