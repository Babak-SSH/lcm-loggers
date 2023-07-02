#include <iostream>

#include <lcm/lcm-cpp.hpp>

#include "./lcm_types/cpp/IMU_t.hpp"
#include "./lcm_types/cpp/motor_command_t.hpp"
#include "./lcm_types/cpp/contact_t.hpp"


int main(int argc, char ** argv){
    std::string filePath;
    bool m, i, c, a, p, t;
    if (argc >= 2){
        for(int i=0;i<argc;i++){
            if(std::string(argv[i]) == "-h" || std::string(argv[i]) == "--help"){
                std::cout << "reads the recorded logs of actuators and other sensors and shows simple graph of the outputs.";
                std::cout << "[-m] : Shows logs of Motors.";
                std::cout << "[-i] : Shows logs of IMU.";
                std::cout << "[-c] : Shows logs of Contact sensor.";
                std::cout << "[-a] : Shows logs all types of output.";
                std::cout << "[-f] : LCM log file path.";
                std::cout << "[-p] : Plot the selected data.";
                std::cout << "[-t] : show the outputs in terminal.";

            }
            if(std::string(argv[i]) == "-m" || std::string(argv[i]) == "--Motor"){
                m = true;
            }
            if(std::string(argv[i]) == "-i" || std::string(argv[i]) == "--Imu"){
                m = true;
            }
            if(std::string(argv[i]) == "-c" || std::string(argv[i]) == "--Contact"){
                m = true;
            }
            if(std::string(argv[i]) == "-a" || std::string(argv[i]) == "--All"){
                m = true;
            }
            if(std::string(argv[i]) == "-f" || std::string(argv[i]) == "--File"){
                m = true;
            }
            if(std::string(argv[i]) == "-p" || std::string(argv[i]) == "--Plot"){
                m = true;
            }
            if(std::string(argv[i]) == "-t" || std::string(argv[i]) == "--Terminal"){
                m = true;
            }
        }
    }
    
    lcm::LCM lcm;

    if(!lcm.good())
        return 1;

    return 0;
}