import os
import pathlib
from launch import LaunchDescription
from launch_ros.actions import Node

LOG_LEVEL='debug'

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
                parameters=config_list,
                output='screen',
                emulate_tty=True,
                arguments=[('__log_level:='+LOG_LEVEL)],
                respawn=True
            )
        )

    def get_launch_description(self):
        return self.ld