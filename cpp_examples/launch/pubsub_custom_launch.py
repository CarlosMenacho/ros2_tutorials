import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='cpp_examples',
            executable='pub_custom',
            name='pub_custom'),

        launch_ros.actions.Node(
            package='cpp_examples',
            executable='sub_custom',
            name='sub_custom'),
  ])