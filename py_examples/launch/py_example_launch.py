import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='py_examples',
            executable='publipy',
            name='publipy'),

        launch_ros.actions.Node(
            package='py_examples',
            executable='subpy',
            name='subpy'),
  ])