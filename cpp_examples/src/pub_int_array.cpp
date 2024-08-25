#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/int8_multi_array.hpp>

using namespace std::chrono_literals;

class MyPublisher : public rclcpp::Node
{
    rclcpp::Publisher<std_msgs::msg::Int8MultiArray>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int a = 0, b = 78, c = 0;

public:
    MyPublisher() : Node("my_publisher")
    {
        publisher_ = this->create_publisher<std_msgs::msg::Int8MultiArray>("carlos_m", 10);
        timer_ = this->create_wall_timer(1000ms, std::bind(&MyPublisher::publish_data, this));
    }

private:
    void publish_data()
    {
        std_msgs::msg::Int8MultiArray msg;
        // Populate the data array with your values
        msg.data.push_back(a); // First value
        msg.data.push_back(b); // Second value
        msg.data.push_back(c); // Third value
        a++;
        c--;

        publisher_->publish(msg);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MyPublisher>());
    rclcpp::shutdown();
    return 0;
}