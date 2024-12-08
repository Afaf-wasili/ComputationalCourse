/*Q3: Write a Python script that uses the math library to perform the following calculations:

1. Calculate the Area of a Circle:

A. Write a function named circle_area(radius) that takes the radius of a circle as input and returns the area of the circle. Use the formula area = math.pi * radius**2.

2. Calculate the Volume of a Sphere:

Write a function named sphere_volume(radius) that takes the radius of a sphere as input and returns the volume of the sphere. Use the formula volume = (4/3) * math.pi * radius**3.

3. Main Script:
A. Prompt the user to enter the radius of a circle and a sphere.
B. Use the circle_area and sphere_volume functions to calculate the area and volume, respectively.
C. Print the results with appropriate labels.

Ensure that the script correctly performs these calculations and handles user input.
*/


#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double circle_radius, sphere_radius;

    cout << "Enter the radius of the circle: ";
    cin >> circle_radius;
    cout << "Area of the circle: " << M_PI * circle_radius * circle_radius << endl;

    cout << "Enter the radius of the sphere: ";
    cin >> sphere_radius;
    cout << "Volume of the sphere: " << (4.0 / 3.0) * M_PI * pow(sphere_radius, 3) << endl;

    return 0;
}


