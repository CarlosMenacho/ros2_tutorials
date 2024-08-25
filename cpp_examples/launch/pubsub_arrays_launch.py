import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='cpp_examples',
            executable='pub_array',
            name='pub_array'),

        launch_ros.actions.Node(
            package='cpp_examples',
            executable='sub_array',
            name='sub_array'),

  ])