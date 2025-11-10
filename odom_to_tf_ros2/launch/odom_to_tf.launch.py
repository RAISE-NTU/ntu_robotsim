from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'log_level',
            default_value='info',
            description='Logging level',
        ),
        Node(
            package='odom_to_tf_ros2', 
            executable='odom_to_tf',   
            name='odom_to_tf',
            output='screen',
            parameters=[
                {'odom_topic': '/odom_ground_truth'},
                {'use_sim_time': True},
            ],
            arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=[
                '0', '0', '0',  # Translation: x y z
                '0', '0', '0', '1',  # Rotation: qx qy qz qw
                'base_link',  # Parent frame
                'realsense'  # Child frame
            ],
            parameters=[
                {'use_sim_time': True},
            ],
            output='screen'
        ),
    ])
