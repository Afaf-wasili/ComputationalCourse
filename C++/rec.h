class Rectangle{

private:
  double length  ;
  double width ;

public:
  Rectangle(double x, double y) : length(x), width(y) {}

  double get_area(){
    return length * width;
  }
  double get_perimeter(){
    return 2 * (length * width);
  }


};
