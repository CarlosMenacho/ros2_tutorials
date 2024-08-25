#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/int8_multi_array.hpp>

class MySubscriber : public rclcpp::Node
{
    rclcpp::Subscription<std_msgs::msg::Int8MultiArray>::SharedPtr subscription_;

public:
    MySubscriber() : Node("my_subscriber")
    {
        subscription_ = this->create_subscription<std_msgs::msg::Int8MultiArray>(
            "carlos_m", 10, std::bind(&MySubscriber::topic_callback, this, std::placeholders::_1));
    }

private:
    void topic_callback(const std_msgs::msg::Int8MultiArray::SharedPtr msg)
    {
        // Process the received data here
        RCLCPP_INFO(this->get_logger(), "Received values: %d, %d, %d",
                    msg->data[0], msg->data[1], msg->data[2]);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MySubscriber>());
    rclcpp::shutdown();
    return 0;
}
