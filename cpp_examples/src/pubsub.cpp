#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

class MinimalPubSub : public rclcpp::Node
{
    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t count_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscriber;

public:
    MinimalPubSub()
        : Node("PubSub"), count_(0)
    {
        // publisher
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic2", 10);
        timer_ = this->create_wall_timer(500ms, std::bind(&MinimalPubSub::timer_callback, this));

        // subscriber
        subscriber = this->create_subscription<std_msgs::msg::String>("topic1", 10, std::bind(&MinimalPubSub::topic_callback, this, _1));
    }

private:
    void timer_callback()
    {
        auto message = std_msgs::msg::String();
        message.data = "Sending from pubsub Node" + std::to_string(count_++);
        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        publisher_->publish(message);
    }
    void topic_callback(const std_msgs::msg::String &msg) const
    {
        RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg.data.c_str());
    }
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalPubSub>());
    rclcpp::shutdown();
    return 0;
}