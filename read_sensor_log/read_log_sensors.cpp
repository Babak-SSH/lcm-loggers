#include <asm-generic/errno.h>
#include <iostream>
#include <vector>
#include <map>

#include <lcm/lcm-cpp.hpp>

#include "../lcm_types/cpp/IMU_t.hpp"
#include "../lcm_types/cpp/motor_response_t.hpp"
#include "../lcm_types/cpp/contact_t.hpp"


int main(int argc, char ** argv){
    std::string filePath;
    bool m, i, c, a, p, t;

    std::vector<bool> contactData;
    std::vector<double> contactTimestamp;
    
    std::vector<double> dataAccX;
    std::vector<double> dataAccY;
    std::vector<double> dataAccZ;
    std::vector<double> imuTimestamp;

    std::map<char, std::vector<double>> dataMotorP;
    std::map<char, std::vector<double>> motorTimestamps;

    std::vector<char> motorIDs = {'1', '2','5'};

    for (auto it = motorIDs.begin(); it != motorIDs.end(); it++){
        dataMotorP[*it] = std::vector<double>();
    }

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
                std::cout << "[-t] : show the outputs in terminal.\n";

            }
            if(std::string(argv[i]) == "-m" || std::string(argv[i]) == "--Motor"){
                m = true;
            }
            if(std::string(argv[i]) == "-i" || std::string(argv[i]) == "--Imu"){
                i = true;
            }
            if(std::string(argv[i]) == "-c" || std::string(argv[i]) == "--Contact"){
                c = true;
            }
            if(std::string(argv[i]) == "-a" || std::string(argv[i]) == "--All"){
                a = true;
            }
            if(std::string(argv[i]) == "-f" || std::string(argv[i]) == "--File"){
                i++;
                filePath = argv[i];
            }
            if(std::string(argv[i]) == "-p" || std::string(argv[i]) == "--Plot"){
                p = true;
            }
            if(std::string(argv[i]) == "-t" || std::string(argv[i]) == "--Terminal"){
                m = true;
            }
        }
    }

    // Open the log file.
    lcm::LogFile log(filePath, "r");
    if (!log.good()) {
        perror("LogFile");
        fprintf(stderr, "couldn't open log file %s\n", argv[1]);
        return 1;
    }

    while (1) {
        // Read a log event.
        const lcm::LogEvent *event = log.readNextEvent();
        if (!event)
            break;

        // Only process messages on the MOTOR_RESPONSE channel.
        if ((a || m) && event->channel == "MOTOR_RESPONSE"){
            // Try to decode the message.
            motor_response_t msg;
            if (msg.decode(event->data, 0, event->datalen) != event->datalen)
                continue;

            dataMotorP[msg.id].push_back(msg.p); 
            motorTimestamps[msg.id].push_back((long long)(event->timestamp/1000));

            if (t){
                printf("motor data:");
                printf("   timestamp   = %lld", (long long)(event->timestamp/1000));
                printf("   id       = %f", msg.id);
                printf("   p        = %f", msg.p);
                printf("   v        = %f", msg.v);
                printf("   i        = %f\n", msg.i);
            }
        }
        else if((a || i) && event->channel == "IMU_ACC"){
            IMU_t msg;
            if (msg.decode(event->data, 0, event->datalen) != event->datalen)
                continue;

            dataAccX.push_back(msg.acc_x);
            dataAccY.push_back(msg.acc_y);
            dataAccZ.push_back(msg.acc_z);
            imuTimestamp.push_back((long long)(event->timestamp/1000));
        
            if (t){
                printf("imu data:");
                printf("   timestamp   = %lld",(long long)(event->timestamp/1000));
                printf("   acc_x       = %f",(msg.acc_x));
                printf("   acc_y       = %f",(msg.acc_y));
                printf("   acc_z       = %f\n",(msg.acc_z));
            }
        }
        else if((a || c) && event->channel == "CONTACT"){
            contact_t msg;
            if (msg.decode(event->data, 0, event->datalen) != event->datalen)
                continue;

            contactData.push_back(msg.touch);
            contactTimestamp.push_back((long long)(event->timestamp/1000));

            if (t){
                printf("contact data:");
                printf("   timestamp   = %lld", (long long)(event->timestamp/1000));
                printf("   touch       = %d\n", msg.touch);
            }
        }
    }

    return 0;
}