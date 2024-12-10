#include "class.h" 


// Main function
int Classh() {
    Rectangle both(23, 24); // Create a Rectangle object 'rec' with length 23 and width 24
          
    // Output the area and perimeter of the rectangle
     std::cout << "Area = " <<  both.get_area()  << std::endl;
     std::cout << "Perimeter = " << both.get_perimeter() << std::endl;
             
    return 0; // Return 0 to indicate successful execution
}