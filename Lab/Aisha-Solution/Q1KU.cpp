//Question: Define the variables x and y in separate header file

#include "Q1KU.h"
void Q1KU(){
    if (x < y) {
        std::cout << x << " is less than " << y << std::endl;
    } else if (x > y) {
        std::cout << x << " is greater than " << y << std::endl;
    } else {
        std::cout << x << " and " << y << " are equal" << std::endl;
    }
}


