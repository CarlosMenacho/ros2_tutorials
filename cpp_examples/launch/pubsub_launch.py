import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='cpp_examples',
            executable='publisher',
            name='publisher'),

        launch_ros.actions.Node(
            package='cpp_examples',
            executable='pubsub',
            name='pubsub'),

        launch_ros.actions.Node(
            package='cpp_examples',
            executable='subscriber',
            name='subscriber'),
  ])