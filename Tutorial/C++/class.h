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


