cmake_minimum_required(VERSION 3.8)
project(cpp_examples)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
# Adding the custom interface
find_package(custom_interface REQUIRED)

add_executable(publisher src/pub.cpp)
ament_target_dependencies(publisher rclcpp std_msgs)

add_executable(subscriber src/sub.cpp)
ament_target_dependencies(subscriber rclcpp std_msgs)

add_executable(pubsub src/pubsub.cpp)
ament_target_dependencies(pubsub rclcpp std_msgs)

add_executable(pub_array src/pub_int_array.cpp)
ament_target_dependencies(pub_array rclcpp std_msgs)

add_executable(sub_array src/sub_int_array.cpp)
ament_target_dependencies(sub_array rclcpp std_msgs)

# Make sure to add the custom interface to our executables
add_executable(pub_custom src/custom_msg_pub.cpp)
ament_target_dependencies(pub_custom rclcpp custom_interface ) 

add_executable(sub_custom src/custom_msg_sub.cpp)
ament_target_dependencies(sub_custom rclcpp custom_interface ) 

add_executable(server src/service_example.cpp)
ament_target_dependencies(server rclcpp custom_interface )    

add_executable(client src/client_example.cpp)
ament_target_dependencies(client rclcpp custom_interface )   

install(TARGETS
  publisher
  subscriber
  pubsub
  pub_array
  sub_array
  pub_custom
  sub_custom
  server
  client
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
