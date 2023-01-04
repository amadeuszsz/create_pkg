# Copyright YEAR MAINTAINER_NAME
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
    pkg_prefix = get_package_share_directory("hello_world")

    config_param = DeclareLaunchArgument(
        'config_param_file',
        default_value=[pkg_prefix, '/param/defaults.param.yaml'],
        description='Node config.'
    )

    hello_world_node = Node(
            name='hello_world_node',
            namespace='',
            package='hello_world',
            executable='hello_world_node.py',
            parameters=[
                LaunchConfiguration('config_param_file')
            ],
            output='screen',
            arguments=['--ros-args', '--log-level', 'info', '--enable-stdout-logs'],
            emulate_tty=True
    )

    return LaunchDescription([
        config_param,
        hello_world_node
        ])
