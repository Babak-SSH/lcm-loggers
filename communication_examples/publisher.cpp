#include <lcm/lcm-cpp.hpp>
#include "../lcm_types/cpp/example_t.hpp"

int main(int argc, char ** argv)
{
    lcm::LCM lcm;
    if(!lcm.good())
        return 1;

    example_t msg;
    msg.counter = 1;

    lcm.publish("EXAMPLE", &msg);

    return 0;
}