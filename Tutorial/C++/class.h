//class: many functions
//define the rectangle
class Rectangle{ // name of the class

private: //varaibles
  double length;
  double width;


public: //initialize a rectangle class
  Rectangle(double x, double y): length(x), width(y) {}

  //first function definition
  double get_area(){
    return length * width;
  }

  //second function definition
  double get_perimeter(){
    return 2 * (length+ width);
  }
};
