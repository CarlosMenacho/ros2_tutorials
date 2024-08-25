#include "rclcpp/rclcpp.hpp"
#include "custom_interface/srv/add_three_ints.hpp"  // Ensure this path is correct

#include <memory>

void add(const std::shared_ptr<custom_interface::srv::AddThreeInts::Request> request,
         std::shared_ptr<custom_interface::srv::AddThreeInts::Response> response)
{
  response->sum = request->a + request->b + request->c;
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Incoming request\na: %ld b: %ld c: %ld",
              request->a, request->b, request->c);
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "sending back response: [%ld]", response->sum);
}

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  auto node = rclcpp::Node::make_shared("add_three_ints_server");

  auto service = node->create_service<custom_interface::srv::AddThreeInts>(
    "add_three_ints", &add);

  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready to add three ints.");

  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
