
// Define the Rectangle class
class Rectangle {
private:
    double length; // Length of the rectangle
    double width;  // Width of the rectangle

public:
    // Constructor to initialize a Rectangle object with length and width
    Rectangle(double x, double y) : length(x), width(y) {}

    // Method to calculate and return the area of the rectangle
    double get_area() {
        return length * width; // Area is calculated as length times width
    }

    // Method to calculate and return the perimeter of the rectangle
     double get_perimeter() {
     return 2 * (length + width); // Correct formula for perimeter
 }
};

// Main function
double  Class() {
    Rectangle both(23, 24); // Create a Rectangle object 'rec' with length 23 and width 24
     
    // Output the area and perimeter of the rectangle
     std::cout << "Area = " <<  both.get_area()  << std::endl;
    std::cout << "Perimeter = " << both.get_perimeter() << std::endl;

    return 0; // Return 0 to indicate successful execution
}


